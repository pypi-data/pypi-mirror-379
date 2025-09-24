# -*- coding: utf-8 -*-
# This file is part of Xpra.
# Copyright (C) 2011-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import os.path
import cairo
import gi
from typing import Dict, Tuple, Any, Optional, Callable

from xpra.util import first_time, envint, envbool, print_nested_dict
from xpra.os_util import strtobytes, WIN32, OSX, POSIX, is_X11
from xpra.version_util import parse_version
from xpra.log import Logger

gi.require_version("Gdk", "3.0")  # @UndefinedVariable
gi.require_version("Gtk", "3.0")  # @UndefinedVariable
gi.require_version("Pango", "1.0")  # @UndefinedVariable
gi.require_version("GdkPixbuf", "2.0")  # @UndefinedVariable
from gi.repository import GLib, GdkPixbuf, Pango, GObject, Gtk, Gdk     #@UnresolvedImport

log = Logger("gtk", "util")
screenlog = Logger("gtk", "screen")
alphalog = Logger("gtk", "alpha")

SHOW_ALL_VISUALS = False
#try to get workarea from GTK:
GTK_WORKAREA = envbool("XPRA_GTK_WORKAREA", True)

GTK_VERSION_INFO : Dict[str,Dict[str,Tuple]] = {}
def get_gtk_version_info() -> Dict[str,Any]:
    #update props given:
    global GTK_VERSION_INFO
    def av(k, v):
        GTK_VERSION_INFO[k] = {"version" : parse_version(v)}
    def V(k, module, attr_name):
        v = getattr(module, attr_name, None)
        if v is not None:
            av(k, v)
            return True
        return False

    if not GTK_VERSION_INFO:
        V("gobject",    GObject,    "pygobject_version")
        #this isn't the actual version, (only shows as "3.0")
        #but still better than nothing:
        V("gi",         gi,         "__version__")
        V("gtk",        Gtk,        "_version")
        V("gdk",        Gdk,        "_version")
        V("gobject",    GObject,    "_version")
        V("pixbuf",     GdkPixbuf,     "_version")
        V("pixbuf",     GdkPixbuf,     "PIXBUF_VERSION")
        def MAJORMICROMINOR(name, module):
            try:
                v = tuple(getattr(module, x) for x in ("MAJOR_VERSION", "MICRO_VERSION", "MINOR_VERSION"))
                av(name, ".".join(str(x) for x in v))
            except Exception:
                pass
        MAJORMICROMINOR("gtk",  Gtk)
        MAJORMICROMINOR("glib", GLib)
        av("cairo", parse_version(cairo.version_info))  #pylint: disable=no-member
        av("pango", parse_version(Pango.version_string()))
    return GTK_VERSION_INFO.copy()


def pixbuf_save_to_memory(pixbuf, fmt="png") -> bytes:
    buf = []
    def save_to_memory(data, *_args, **_kwargs):
        buf.append(strtobytes(data))
        return True
    pixbuf.save_to_callbackv(save_to_memory, None, fmt, [], [])
    return b"".join(buf)


def GDKWindow(*args, **kwargs) -> Gdk.Window:
    return new_GDKWindow(Gdk.Window, *args, **kwargs)

def new_GDKWindow(gdk_window_class,
                  parent=None, width=1, height=1, window_type=Gdk.WindowType.TOPLEVEL,
                  event_mask=0, wclass=Gdk.WindowWindowClass.INPUT_OUTPUT, title=None,
                  x=None, y=None, override_redirect=False, visual=None) -> Gdk.Window:
    attributes_mask = 0
    attributes = Gdk.WindowAttr()
    if x is not None:
        attributes.x = x
        attributes_mask |= Gdk.WindowAttributesType.X
    if y is not None:
        attributes.y = y
        attributes_mask |= Gdk.WindowAttributesType.Y
    #attributes.type_hint = Gdk.WindowTypeHint.NORMAL
    #attributes_mask |= Gdk.WindowAttributesType.TYPE_HINT
    attributes.width = width
    attributes.height = height
    attributes.window_type = window_type
    if title:
        attributes.title = title
        attributes_mask |= Gdk.WindowAttributesType.TITLE
    if visual:
        attributes.visual = visual
        attributes_mask |= Gdk.WindowAttributesType.VISUAL
    #OR:
    attributes.override_redirect = override_redirect
    attributes_mask |= Gdk.WindowAttributesType.NOREDIR
    #events:
    attributes.event_mask = event_mask
    #wclass:
    attributes.wclass = wclass
    mask = Gdk.WindowAttributesType(attributes_mask)
    return gdk_window_class(parent, attributes, mask)

def set_visual(window, alpha : bool=True) -> Optional[Gdk.Visual]:
    screen = window.get_screen()
    if alpha:
        visual = screen.get_rgba_visual()
    else:
        visual = screen.get_system_visual()
    alphalog("set_visual(%s, %s) screen=%s, visual=%s", window, alpha, screen, visual)
    #we can't do alpha on win32 with plain GTK,
    #(though we handle it in the opengl backend)
    l : Callable = alphalog.warn
    if WIN32 or not first_time("no-rgba"):
        l = alphalog.debug
    if alpha and visual is None or (not WIN32 and not screen.is_composited()):
        l("Warning: cannot handle window transparency")
        if visual is None:
            l(" no RGBA visual")
        else:
            assert not screen.is_composited()
            l(" screen is not composited")
        return None
    alphalog("set_visual(%s, %s) using visual %s", window, alpha, visual)
    if visual:
        window.set_visual(visual)
    return visual


def get_pixbuf_from_data(rgb_data, has_alpha : bool, w : int, h : int, rowstride : int) -> GdkPixbuf.Pixbuf:
    data = GLib.Bytes(rgb_data)
    return GdkPixbuf.Pixbuf.new_from_bytes(data, GdkPixbuf.Colorspace.RGB,
                                           has_alpha, 8, w, h, rowstride)

def color_parse(*args) -> Optional[Gdk.Color]:
    v = Gdk.RGBA()
    ok = v.parse(*args)
    if ok:
        return v.to_color()  # pylint: disable=no-member
    ok, v = Gdk.Color.parse(*args)
    if ok:
        return v
    return None

def get_default_root_window() -> Optional[Gdk.Window]:
    screen = Gdk.Screen.get_default()
    if screen is None:
        return None
    return screen.get_root_window()

def get_root_size(default:Tuple[int,int]=(1920, 1024)) -> Tuple[int,int]:
    if OSX:
        #the easy way:
        root = get_default_root_window()
        if not root:
            return default
        w, h = root.get_geometry()[2:4]
    else:
        #GTK3 on win32 triggers this warning:
        #"GetClientRect failed: Invalid window handle."
        #if we try to use the root window,
        #and on Linux with Wayland, we get bogus values...
        screen = Gdk.Screen.get_default()
        if screen is None:
            return default
        w = screen.get_width()
        h = screen.get_height()
    if w<=0 or h<=0 or w>32768 or h>32768:
        if first_time("Gtk root window dimensions"):
            log.warn(f"Warning: Gdk returned invalid root window dimensions: {w}x{h}")
            w, h = default
            log.warn(f" using {w}x{h} instead")
            if WIN32:
                log.warn(" no access to the display?")
    return w, h

def get_default_cursor() -> Gdk.Cursor:
    display = Gdk.Display.get_default()
    return Gdk.Cursor.new_from_name(display, "default")

BUTTON_MASK : Dict[int, int] = {
    Gdk.ModifierType.BUTTON1_MASK : 1,
    Gdk.ModifierType.BUTTON2_MASK : 2,
    Gdk.ModifierType.BUTTON3_MASK : 3,
    Gdk.ModifierType.BUTTON4_MASK : 4,
    Gdk.ModifierType.BUTTON5_MASK : 5,
    }

em = Gdk.EventMask
WINDOW_EVENT_MASK = em.STRUCTURE_MASK | em.KEY_PRESS_MASK | em.KEY_RELEASE_MASK \
        | em.POINTER_MOTION_MASK | em.BUTTON_PRESS_MASK | em.BUTTON_RELEASE_MASK \
        | em.PROPERTY_CHANGE_MASK | em.SCROLL_MASK

del em


orig_pack_start = Gtk.Box.pack_start
def pack_start(self, child, expand=True, fill=True, padding=0):
    orig_pack_start(self, child, expand, fill, padding)
Gtk.Box.pack_start = pack_start

GRAB_STATUS_STRING = {
    Gdk.GrabStatus.SUCCESS          : "SUCCESS",
    Gdk.GrabStatus.ALREADY_GRABBED  : "ALREADY_GRABBED",
    Gdk.GrabStatus.INVALID_TIME     : "INVALID_TIME",
    Gdk.GrabStatus.NOT_VIEWABLE     : "NOT_VIEWABLE",
    Gdk.GrabStatus.FROZEN           : "FROZEN",
    }

VISUAL_NAMES = {
    Gdk.VisualType.STATIC_GRAY      : "STATIC_GRAY",
    Gdk.VisualType.GRAYSCALE        : "GRAYSCALE",
    Gdk.VisualType.STATIC_COLOR     : "STATIC_COLOR",
    Gdk.VisualType.PSEUDO_COLOR     : "PSEUDO_COLOR",
    Gdk.VisualType.TRUE_COLOR       : "TRUE_COLOR",
    Gdk.VisualType.DIRECT_COLOR     : "DIRECT_COLOR",
    }

BYTE_ORDER_NAMES = {
                Gdk.ByteOrder.LSB_FIRST   : "LSB",
                Gdk.ByteOrder.MSB_FIRST   : "MSB",
                }


def get_screens_info() -> Dict[int,Dict]:
    display = Gdk.Display.get_default()
    info : Dict[int,Dict] = {}
    assert display.get_n_screens()==1, "GTK3: The number of screens is always 1"
    screen = display.get_screen(0)
    info[0] = get_screen_info(display, screen)
    return info

def get_screen_sizes(xscale:float=1, yscale:float=1):
    from xpra.platform.gui import get_workarea, get_workareas
    def xs(v):
        return round(v/xscale)
    def ys(v):
        return round(v/yscale)
    def swork(*workarea):
        return xs(workarea[0]), ys(workarea[1]), xs(workarea[2]), ys(workarea[3])
    display = Gdk.Display.get_default()
    if not display:
        return ()
    MIN_DPI = envint("XPRA_MIN_DPI", 10)
    MAX_DPI = envint("XPRA_MIN_DPI", 500)
    def dpi(size_pixels, size_mm):
        if size_mm==0:
            return 0
        return round(size_pixels * 254 / size_mm / 10)
    #GTK 3.22 onwards always returns just a single screen,
    #potentially with multiple monitors
    n_monitors = display.get_n_monitors()
    workareas = get_workareas()
    if workareas and len(workareas)!=n_monitors:
        screenlog(" workareas: %s", workareas)
        screenlog(" number of monitors does not match number of workareas!")
        workareas = []
    monitors = []
    for j in range(n_monitors):
        monitor = display.get_monitor(j)
        geom = monitor.get_geometry()
        manufacturer, model = monitor.get_manufacturer(), monitor.get_model()
        if manufacturer in ("unknown", None):
            manufacturer = ""
        if model in ("unknown", None):
            model = ""
        if manufacturer and model:
            plug_name = "%s %s" % (manufacturer, model)
        elif manufacturer:
            plug_name = manufacturer
        elif model:
            plug_name = model
        else:
            plug_name = "%i" % j
        wmm, hmm = monitor.get_width_mm(), monitor.get_height_mm()
        monitor_info = [plug_name, xs(geom.x), ys(geom.y), xs(geom.width), ys(geom.height), wmm, hmm]
        screenlog(" monitor %s: %s, model=%s, manufacturer=%s",
                  j, type(monitor).__name__, monitor.get_model(), monitor.get_manufacturer())
        def vmwx(v):
            return v<geom.x or v>geom.x+geom.width
        def vmwy(v):
            return v<geom.y or v>geom.y+geom.height
        def valid_workarea(work_x, work_y, work_width, work_height):
            if vmwx(work_x) or vmwx(work_x+work_width) or vmwy(work_y) or vmwy(work_y+work_height):
                log("discarding invalid workarea: %s", (work_x, work_y, work_width, work_height))
                return []
            return list(swork(work_x, work_y, work_width, work_height))
        if GTK_WORKAREA and hasattr(monitor, "get_workarea"):
            rect = monitor.get_workarea()
            monitor_info += valid_workarea(rect.x, rect.y, rect.width, rect.height)
        elif workareas:
            monitor_info += valid_workarea(*workareas[j])
        monitors.append(tuple(monitor_info))
    screen = display.get_default_screen()
    sw, sh = screen.get_width(), screen.get_height()
    work_x, work_y, work_width, work_height = swork(0, 0, sw, sh)
    workarea = get_workarea()   #pylint: disable=assignment-from-none
    screenlog(" workarea=%s", workarea)
    if workarea:
        work_x, work_y, work_width, work_height = swork(*workarea)  #pylint: disable=not-an-iterable
        def vwx(v):
            return v<0 or v>sw
        def vwy(v):
            return v<0 or v>sh
        if vwx(work_x) or vwx(work_x+work_width) or vwy(work_y) or vwy(work_y+work_height):
            screenlog(" discarding invalid workarea values: %s", workarea)
            work_x, work_y, work_width, work_height = swork(0, 0, sw, sh)
    wmm = screen.get_width_mm()
    hmm = screen.get_height_mm()
    xdpi = dpi(sw, wmm)
    ydpi = dpi(sh, hmm)
    if xdpi<MIN_DPI or xdpi>MAX_DPI or ydpi<MIN_DPI or ydpi>MAX_DPI:
        log(f"ignoring invalid DPI {xdpi},{ydpi} from screen size {wmm}x{hmm}mm")
        if os.environ.get("WAYLAND_DISPLAY"):
            log(" (wayland display?)")
        if n_monitors>0:
            wmm = 0
            for mi in range(n_monitors):
                monitor = display.get_monitor(mi)
                log(" monitor %i: %s, model=%s, manufacturer=%s",
                    mi, monitor, monitor.get_model(), monitor.get_manufacturer())
                wmm += monitor.get_width_mm()
                hmm += monitor.get_height_mm()
            wmm /= n_monitors
            hmm /= n_monitors
            xdpi = dpi(sw, wmm)
            ydpi = dpi(sh, hmm)
        if xdpi<MIN_DPI or xdpi>MAX_DPI or ydpi<MIN_DPI or ydpi>MAX_DPI:
            #still invalid, generate one from DPI=96
            wmm = round(sw*25.4/96)
            hmm = round(sh*25.4/96)
        log(" using %ix%i mm", wmm, hmm)
    screen0 = (screen.make_display_name(), xs(sw), ys(sh),
                wmm, hmm,
                monitors,
                work_x, work_y, work_width, work_height)
    screenlog(" screen: %s", screen0)
    return [screen0]

def get_screen_info(display, screen) -> Dict[str,Any]:
    info = {}
    if not WIN32:
        try:
            w = screen.get_root_window()
            if w:
                info["root"] = w.get_geometry()
        except Exception:
            pass
    info["name"] = screen.make_display_name()
    for x in ("width", "height", "width_mm", "height_mm", "resolution", "primary_monitor"):
        fn = getattr(screen, "get_"+x)
        try:
            info[x] = int(fn())
        except Exception:
            pass
    info["monitors"] = display.get_n_monitors()
    m_info = info.setdefault("monitor", {})
    for i in range(screen.get_n_monitors()):
        m_info[i] = get_screen_monitor_info(screen, i)
    fo = screen.get_font_options()
    #win32 and osx return nothing here...
    if fo:
        fontoptions = info.setdefault("fontoptions", {})
        fontoptions.update(get_font_info(fo))
    vinfo = info.setdefault("visual", {})
    def visual(name, v):
        i = get_visual_info(v)
        if i:
            vinfo[name] = i
    visual("rgba", screen.get_rgba_visual())
    visual("system_visual", screen.get_system_visual())
    if SHOW_ALL_VISUALS:
        for i, v in enumerate(screen.list_visuals()):
            visual(i, v)
    #Gtk.settings
    def get_setting(key, gtype):
        v = GObject.Value()
        v.init(gtype)
        if screen.get_setting(key, v):
            return v.get_value()
        return None
    sinfo = info.setdefault("settings", {})
    for x, gtype in {
        #NET:
        "enable-event-sounds"   : GObject.TYPE_INT,
        "icon-theme-name"       : GObject.TYPE_STRING,
        "sound-theme-name"      : GObject.TYPE_STRING,
        "theme-name"            : GObject.TYPE_STRING,
        #Xft:
        "xft-antialias" : GObject.TYPE_INT,
        "xft-dpi"       : GObject.TYPE_INT,
        "xft-hinting"   : GObject.TYPE_INT,
        "xft-hintstyle" : GObject.TYPE_STRING,
        "xft-rgba"      : GObject.TYPE_STRING,
        }.items():
        try:
            v = get_setting("gtk-"+x, gtype)
        except Exception:
            log("failed to query screen '%s'", x, exc_info=True)
            continue
        if v is None:
            v = ""
        if x.startswith("xft-"):
            x = x[4:]
        sinfo[x] = v
    return info

FONT_CONV : Dict[str,Dict[Any,Any]] = {
    "antialias" : {
        cairo.ANTIALIAS_DEFAULT     : "default",
        cairo.ANTIALIAS_NONE        : "none",
        cairo.ANTIALIAS_GRAY        : "gray",
        cairo.ANTIALIAS_SUBPIXEL    : "subpixel",
        },
    "hint_metrics" : {
        cairo.HINT_METRICS_DEFAULT  : "default",
        cairo.HINT_METRICS_OFF      : "off",
        cairo.HINT_METRICS_ON       : "on",
        },
    "hint_style" : {
        cairo.HINT_STYLE_DEFAULT    : "default",
        cairo.HINT_STYLE_NONE       : "none",
        cairo.HINT_STYLE_SLIGHT     : "slight",
        cairo.HINT_STYLE_MEDIUM     : "medium",
        cairo.HINT_STYLE_FULL       : "full",
        },
    "subpixel_order": {
        cairo.SUBPIXEL_ORDER_DEFAULT    : "default",
        cairo.SUBPIXEL_ORDER_RGB        : "RGB",
        cairo.SUBPIXEL_ORDER_BGR        : "BGR",
        cairo.SUBPIXEL_ORDER_VRGB       : "VRGB",
        cairo.SUBPIXEL_ORDER_VBGR       : "VBGR",
        }
    }

def get_font_info(font_options) -> Dict[str,Any]:
    #pylint: disable=no-member
    font_info : Dict[str,Any] = {}
    for x,vdict in FONT_CONV.items():
        fn = getattr(font_options, "get_"+x)
        val = fn()
        font_info[x] = vdict.get(val, val)
    return font_info

VINFO_CONV : Dict[str,Dict[Any,str]] = {
        "bits_per_rgb"          : {},
        "byte_order"            : BYTE_ORDER_NAMES,
        "colormap_size"         : {},
        "depth"                 : {},
        "red_pixel_details"     : {},
        "green_pixel_details"   : {},
        "blue_pixel_details"    : {},
        "visual_type"           : VISUAL_NAMES,
        }

def get_visual_info(v) -> Dict[str,Any]:
    if not v:
        return {}
    vinfo : Dict[str,Any] = {}
    for x, vdict in VINFO_CONV.items():
        val = None
        try:
            #ugly workaround for "visual_type" -> "type" for GTK2...
            val = getattr(v, x.replace("visual_", ""))
        except AttributeError:
            try:
                fn = getattr(v, "get_"+x)
            except AttributeError:
                pass
            else:
                val = fn()
        if val is not None:
            vinfo[x] = vdict.get(val, val)
    return vinfo

def get_screen_monitor_info(screen, i) -> Dict[str,Any]:
    info : Dict[str,Any] = {}
    geom = screen.get_monitor_geometry(i)
    for x in ("x", "y", "width", "height"):
        info[x] = getattr(geom, x)
    if hasattr(screen, "get_monitor_plug_name"):
        info["plug_name"] = screen.get_monitor_plug_name(i) or ""
    for x in ("scale_factor", "width_mm", "height_mm", "refresh_rate"):
        fn = getattr(screen, "get_monitor_"+x, None) or getattr(screen, "get_"+x, None)
        if fn:
            info[x] = int(fn(i))
    rectangle = screen.get_monitor_workarea(i)
    workarea_info = info.setdefault("workarea", {})
    for x in ("x", "y", "width", "height"):
        workarea_info[x] = getattr(rectangle, x)
    return info

def get_monitors_info(xscale:float=1, yscale:float=1) -> Dict[int,Any]:
    display = Gdk.Display.get_default()
    info : Dict[int,Any] = {}
    n = display.get_n_monitors()
    for i in range(n):
        minfo = info.setdefault(i, {})
        monitor = display.get_monitor(i)
        minfo["primary"] = monitor.is_primary()
        for attr in (
            "geometry", "refresh-rate", "scale-factor",
            "width-mm", "height-mm",
            "manufacturer", "model",
            "subpixel-layout",  "workarea",
            ):
            getter = getattr(monitor, "get_%s" % attr.replace("-", "_"), None)
            if getter:
                value = getter()
                if value is None:
                    continue
                if isinstance(value, Gdk.Rectangle):
                    value = (round(xscale*value.x), round(yscale*value.y), round(xscale*value.width), round(yscale*value.height))
                elif attr=="width-mm":
                    value = round(xscale*value)
                elif attr=="height-mm":
                    value = round(yscale*value)
                elif attr=="subpixel-layout":
                    value = {
                        Gdk.SubpixelLayout.UNKNOWN          : "unknown",
                        Gdk.SubpixelLayout.NONE             : "none",
                        Gdk.SubpixelLayout.HORIZONTAL_RGB   : "horizontal-rgb",
                        Gdk.SubpixelLayout.HORIZONTAL_BGR   : "horizontal-bgr",
                        Gdk.SubpixelLayout.VERTICAL_RGB     : "vertical-rgb",
                        Gdk.SubpixelLayout.VERTICAL_BGR     : "vertical-bgr",
                        }.get(value, "unknown")
                if isinstance(value, str):
                    value = value.strip()
                minfo[attr] = value
    return info

def get_display_info(xscale=1, yscale=1) -> Dict[str,Any]:
    display = Gdk.Display.get_default()
    def xy(v):
        return round(xscale*v[0]), round(yscale*v[1])
    def avg(v):
        return round((xscale*v+yscale*v)/2)
    root_size = get_root_size()
    info : Dict[str, Any] = {
            "root-size"             : xy(root_size),
            "screens"               : display.get_n_screens(),
            "name"                  : display.get_name(),
            "pointer"               : xy(display.get_pointer()[-3:-1]),
            "devices"               : len(display.list_devices()),
            "default_cursor_size"   : avg(display.get_default_cursor_size()),
            "maximal_cursor_size"   : xy(display.get_maximal_cursor_size()),
            "pointer_is_grabbed"    : display.pointer_is_grabbed(),
            }
    if not WIN32:
        rw = get_default_root_window()
        if rw:
            info["root"] = rw.get_geometry()
    sinfo = info.setdefault("supports", {})
    for x in ("composite", "cursor_alpha", "cursor_color", "selection_notification", "clipboard_persistence", "shapes"):
        f = "supports_"+x
        if hasattr(display, f):
            fn = getattr(display, f)
            sinfo[x]  = fn()
    info["screens"] = get_screens_info()
    info["monitors"] = get_monitors_info(xscale, yscale)
    dm = display.get_device_manager()
    for dt, name in {
        Gdk.DeviceType.MASTER  : "master",
        Gdk.DeviceType.SLAVE   : "slave",
        Gdk.DeviceType.FLOATING: "floating",
        }.items():
        dinfo = info.setdefault("device", {})
        dtinfo = dinfo.setdefault(name, {})
        devices = dm.list_devices(dt)
        for i, d in enumerate(devices):
            dtinfo[i] = d.get_name()
    return info


def scaled_image(pixbuf, icon_size:int=0) -> Optional[Gtk.Image]:
    if not pixbuf:
        return None
    if icon_size:
        pixbuf = pixbuf.scale_simple(icon_size, icon_size, GdkPixbuf.InterpType.BILINEAR)
    return Gtk.Image.new_from_pixbuf(pixbuf)


def get_icon_from_file(filename):
    if not filename:
        log("get_icon_from_file(%s)=None", filename)
        return None
    try:
        if not os.path.exists(filename):
            log.warn("Warning: cannot load icon, '%s' does not exist", filename)
            return None
        with open(filename, mode="rb") as f:
            data = f.read()
        loader = GdkPixbuf.PixbufLoader()
        loader.write(data)
        loader.close()
    except Exception as e:
        log("get_icon_from_file(%s)", filename, exc_info=True)
        log.error("Error: failed to load '%s'", filename)
        log.estr(e)
        return None
    pixbuf = loader.get_pixbuf()
    return pixbuf


def get_icon_pixbuf(icon_name):
    try:
        if not icon_name:
            log("get_icon_pixbuf(%s)=None", icon_name)
            return None
        from xpra.platform.paths import get_icon_filename
        icon_filename = get_icon_filename(icon_name)
        log("get_pixbuf(%s) icon_filename=%s", icon_name, icon_filename)
        if icon_filename:
            return GdkPixbuf.Pixbuf.new_from_file(filename=icon_filename)
    except Exception:
        log.error("get_icon_pixbuf(%s)", icon_name, exc_info=True)
    return None


def imagebutton(title, icon=None, tooltip="", clicked_callback:Optional[Callable]=None, icon_size=32,
                default=False, min_size=None, label_color=None, label_font=None) -> Gtk.Button:
    button = Gtk.Button(label=title)
    settings = button.get_settings()
    settings.set_property('gtk-button-images', True)
    if icon:
        if icon_size:
            icon = scaled_image(icon, icon_size)
        button.set_image(icon)
    if tooltip:
        button.set_tooltip_text(tooltip)
    if min_size:
        button.set_size_request(min_size, min_size)
    if clicked_callback:
        button.connect("clicked", clicked_callback)
    if default:
        button.set_can_default(True)
    if label_color or label_font:
        l = button
        try:
            alignment = button.get_children()[0]
            b_hbox = alignment.get_children()[0]
            l = b_hbox.get_children()[1]
        except (IndexError, AttributeError):
            pass
        if label_color and hasattr(l, "modify_fg"):
            l.modify_fg(Gtk.StateType.NORMAL, label_color)
        if label_font and hasattr(l, "modify_font"):
            l.modify_font(label_font)
    return button

def menuitem(title, image=None, tooltip=None, cb=None) -> Gtk.ImageMenuItem:
    """ Utility method for easily creating an ImageMenuItem """
    menu_item = Gtk.ImageMenuItem()
    menu_item.set_label(title)
    if image:
        menu_item.set_image(image)
        #override gtk defaults: we *want* icons:
        settings = menu_item.get_settings()
        settings.set_property('gtk-menu-images', True)
        if hasattr(menu_item, "set_always_show_image"):
            menu_item.set_always_show_image(True)
    if tooltip:
        menu_item.set_tooltip_text(tooltip)
    if cb:
        menu_item.connect('activate', cb)
    menu_item.show()
    return menu_item


def add_close_accel(window, callback):
    accel_groups = []
    def wa(s, cb):
        accel_groups.append(add_window_accel(window, s, cb))
    wa('<control>F4', callback)
    wa('<Alt>F4', callback)
    wa('Escape', callback)
    return accel_groups

def add_window_accel(window, accel, callback) -> Gtk.AccelGroup:
    def connect(ag, *args):
        ag.connect(*args)
    accel_group = Gtk.AccelGroup()
    key, mod = Gtk.accelerator_parse(accel)
    connect(accel_group, key, mod, Gtk.AccelFlags.LOCKED, callback)
    window.add_accel_group(accel_group)
    return accel_group


def label(text:str="", tooltip=None, font=None) -> Gtk.Label:
    l = Gtk.Label(label=text)
    if font:
        fontdesc = Pango.FontDescription(font)
        l.modify_font(fontdesc)
    if tooltip:
        l.set_tooltip_text(tooltip)
    return l


class TableBuilder:

    def __init__(self, rows=1, columns=2, homogeneous=False, col_spacings=0, row_spacings=0):
        self.table = Gtk.Table(rows, columns, homogeneous)
        self.table.set_col_spacings(col_spacings)
        self.table.set_row_spacings(row_spacings)
        self.row = 0
        self.widget_xalign = 0.0

    def get_table(self):
        return self.table

    def add_row(self, widget, *widgets, **kwargs):
        if widget:
            l_al = Gtk.Alignment(xalign=1.0, yalign=0.5, xscale=0.0, yscale=0.0)
            l_al.add(widget)
            self.attach(l_al, 0)
        if widgets:
            i = 1
            for w in widgets:
                if w:
                    w_al = Gtk.Alignment(xalign=self.widget_xalign, yalign=0.5, xscale=0.0, yscale=0.0)
                    w_al.add(w)
                    self.attach(w_al, i, **kwargs)
                i += 1
        self.inc()

    def attach(self, widget, i=0, count=1,
               xoptions=Gtk.AttachOptions.FILL, yoptions=Gtk.AttachOptions.FILL,
               xpadding=10, ypadding=0):
        self.table.attach(widget, i, i+count, self.row, self.row+1,
                          xoptions=xoptions, yoptions=yoptions, xpadding=xpadding, ypadding=ypadding)

    def inc(self):
        self.row += 1

    def new_row(self, row_label_str="", value1=None, value2=None, label_tooltip=None, **kwargs):
        row_label = label(row_label_str, label_tooltip)
        self.add_row(row_label, value1, value2, **kwargs)


def choose_files(parent_window, title, action=Gtk.FileChooserAction.OPEN, action_button=Gtk.STOCK_OPEN,
                 callback=None, file_filter=None, multiple=True):
    log("choose_files%s", (parent_window, title, action, action_button, callback, file_filter))
    chooser = Gtk.FileChooserDialog(title,
                                parent=parent_window, action=action,
                                buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, action_button, Gtk.ResponseType.OK))
    chooser.set_select_multiple(multiple)
    chooser.set_default_response(Gtk.ResponseType.OK)
    if file_filter:
        chooser.add_filter(file_filter)
    response = chooser.run()
    filenames = chooser.get_filenames()
    chooser.hide()
    chooser.close()
    if response!=Gtk.ResponseType.OK:
        return None
    return filenames

def choose_file(parent_window, title, action=Gtk.FileChooserAction.OPEN, action_button=Gtk.STOCK_OPEN,
                callback=None, file_filter=None) -> Optional[str]:
    filenames = choose_files(parent_window, title, action, action_button, callback, file_filter, False)
    if not filenames or len(filenames)!=1:
        return None
    filename = filenames[0]
    if callback:
        callback(filename)
    return filename


dsinit : bool = False
def init_display_source() -> None:
    """
    On X11, we want to be able to access the bindings,
    so we need to get the X11 display from GDK.
    """
    global dsinit
    dsinit = True
    if is_X11():
        try:
            from xpra.x11.gtk3.gdk_display_source import init_gdk_display_source
            init_gdk_display_source()
        except ImportError:     # pragma: no cover
            from xpra.log import Logger
            log = Logger("gtk", "client")
            log("init_gdk_display_source()", exc_info=True)
            log.warn("Warning: the Gtk-3.0 X11 bindings are missing")
            log.warn(" some features may be degraded or unavailable")
            log.warn(" ie: keyboard mapping, focus, etc")

def ds_inited() -> bool:
    return dsinit


def main():
    from xpra.platform import program_context
    from xpra.log import enable_color
    with program_context("GTK-Version-Info", "GTK Version Info"):
        enable_color()
        print("%s" % get_gtk_version_info())
        if POSIX and not OSX:
            from xpra.x11.bindings.posix_display_source import init_posix_display_source    #@UnresolvedImport
            init_posix_display_source()
        import warnings
        warnings.simplefilter("ignore")
        print(get_screen_sizes()[0])
        print_nested_dict(get_display_info())


if __name__ == "__main__":
    main()
