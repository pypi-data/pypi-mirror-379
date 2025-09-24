# This file is part of Xpra.
# Copyright (C) 2008, 2009 Nathaniel Smith <njs@pobox.com>
# Copyright (C) 2012-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import os
import sys
import logging
import weakref
import itertools
from typing import Callable, Dict, List, Tuple, Any, Set
# This module is used by non-GUI programs and thus must not import gtk.

LOG_PREFIX : str = ""
LOG_FORMAT : str = "%(asctime)s %(message)s"
DEBUG_MODULES : Tuple[str, ...] = ()
if os.name!="posix" or os.getuid()!=0:
    LOG_FORMAT = os.environ.get("XPRA_LOG_FORMAT", LOG_FORMAT)
    LOG_PREFIX = os.environ.get("XPRA_LOG_PREFIX", LOG_PREFIX)
    DEBUG_MODULES = tuple(x.strip() for x in os.environ.get("XPRA_DEBUG_MODULES", "").split(",") if x.strip())
NOPREFIX_FORMAT : str = "%(message)s"


logging.basicConfig(format=LOG_FORMAT)
logging.root.setLevel(logging.INFO)

debug_enabled_categories : Set[str] = set()
debug_disabled_categories : Set[str] = set()

def get_debug_args() -> List[str]:
    args = []
    if debug_enabled_categories:
        args += list(debug_enabled_categories)
    if debug_disabled_categories:
        for x in debug_disabled_categories:
            args.append(f"-{x}")
    return args

class FullDebugContext:
    __slots__ = ("debug_enabled_categories", "enabled")
    def __enter__(self):
        self.debug_enabled_categories = debug_enabled_categories
        debug_enabled_categories.clear()
        debug_enabled_categories.add("all")
        self.enabled = []
        for x in get_all_loggers():
            if not x.is_debug_enabled():
                self.enabled.append(x)
                x.enable_debug()

    def __exit__(self, *_args):
        for x in self.enabled:
            x.disable_debug()
        debug_enabled_categories.clear()
        debug_enabled_categories.update(self.debug_enabled_categories)


def add_debug_category(*cat) -> None:
    remove_disabled_category(*cat)
    for c in cat:
        debug_enabled_categories.add(c)

def remove_debug_category(*cat) -> None:
    for c in cat:
        if c in debug_enabled_categories:
            debug_enabled_categories.remove(c)

def is_debug_enabled(category : str) -> bool:
    if "all" in debug_enabled_categories:
        return True
    if category in debug_enabled_categories:
        return True
    return isenvdebug(category) or isenvdebug("ALL")


def add_disabled_category(*cat) -> None:
    remove_debug_category(*cat)
    for c in cat:
        debug_disabled_categories.add(c)

def remove_disabled_category(*cat) -> None:
    for c in cat:
        if c in debug_disabled_categories:
            debug_disabled_categories.remove(c)


default_level : int = logging.DEBUG
def set_default_level(level:int) -> None:
    global default_level
    default_level = level


def standard_logging(log, level:int, msg:str, *args, **kwargs) -> None:
    #this is just the regular logging:
    log(level, msg, *args, **kwargs)

#this allows us to capture all logging and redirect it:
#the default 'standard_logging' uses the logger,
#but the client may inject its own handler here
global_logging_handler : Callable = standard_logging

def set_global_logging_handler(h:Callable) -> Callable:
    assert callable(h)
    global global_logging_handler
    saved = global_logging_handler
    global_logging_handler = h
    return saved


def setloghandler(lh) -> None:
    logging.root.handlers = []
    logging.root.addHandler(lh)

def enable_color(to=sys.stdout, format_string=NOPREFIX_FORMAT) -> None:
    if not hasattr(to, "fileno"):
        #on win32 sys.stdout can be a "Blackhole",
        #which does not have a fileno
        return
    # pylint: disable=import-outside-toplevel
    #python3 stdout and stderr have a buffer attribute,
    #which we must use if we want to be able to write bytes:
    try:
        import codecs
        sbuf = getattr(to, "buffer", to)
        to = codecs.getwriter("utf-8")(sbuf, "replace")
    except Exception:   # pragma: no cover
        pass
    from xpra.colorstreamhandler import ColorStreamHandler
    csh = ColorStreamHandler(to)
    csh.setFormatter(logging.Formatter(format_string))
    setloghandler(csh)

def enable_format(format_string:str) -> None:
    try:
        logging.root.handlers[0].formatter = logging.Formatter(format_string)
    except (AttributeError, IndexError):
        pass


STRUCT_KNOWN_FILTERS : Dict[str,Dict[str,str]] = {
    "Client" : {
                "client"        : "All client code",
                "paint"         : "Client window paint code",
                "draw"          : "Client draw packets",
                "cairo"         : "Cairo paint code used with the GTK3 client",
                "opengl"        : "Client OpenGL rendering",
                "info"          : "About and Session info dialogs",
                "launcher"      : "The client launcher program",
                },
    "General" : {
                "clipboard"     : "All clipboard operations",
                "notify"        : "Notification forwarding",
                "tray"          : "System Tray forwarding",
                "printing"      : "Printing",
                "file"          : "File transfers",
                "keyboard"      : "Keyboard mapping and key event handling",
                "screen"        : "Screen and workarea dimension",
                "fps"           : "Frames per second",
                "xsettings"     : "XSettings synchronization",
                "dbus"          : "DBUS calls",
                "rpc"           : "Remote Procedure Calls",
                "menu"          : "Menus",
                "events"        : "System and window events",
                },
    "Window" : {
                "window"        : "All window code",
                "damage"        : "Window X11 repaint events",
                "geometry"      : "Window geometry",
                "shape"         : "Window shape forwarding (XShape)",
                "focus"         : "Window focus",
                "workspace"     : "Window workspace synchronization",
                "metadata"      : "Window metadata",
                "alpha"         : "Window Alpha channel (transparency)",
                "state"         : "Window state",
                "icon"          : "Window icons",
                "frame"         : "Window frame",
                "grab"          : "Window grabs (both keyboard and mouse)",
                "dragndrop"     : "Window drag-n-drop events",
                "filters"       : "Window filters",
                },
    "Encoding" : {
                "codec"         : "Codec loader and video helper",
                "loader"        : "Pixel compression codec loader",
                "video"         : "Video encoding",
                "score"         : "Video pipeline scoring and selection",
                "encoding"      : "Server side encoding selection and compression",
                "scaling"       : "Picture scaling",
                "scroll"        : "Scrolling detection and compression",
                "xor"           : "XOR delta pre-compression",
                "subregion"     : "Video subregion processing",
                "regiondetect"  : "Video region detection",
                "regionrefresh" : "Video region refresh",
                "refresh"       : "Refresh of lossy screen updates",
                "compress"      : "Pixel compression",
                },
    "Codec" : {
                #codecs:
                "csc"           : "Colourspace conversion codecs",
                "cuda"          : "CUDA device access",
                "cython"        : "Cython CSC module",
                "swscale"       : "swscale CSC module",
                "libyuv"        : "libyuv CSC module",
                "decoder"       : "All decoders",
                "encoder"       : "All encoders",
                "avcodec"       : "avcodec decoder",
                "libav"         : "libav common code (used by swscale, avcodec and ffmpeg)",
                "ffmpeg"        : "ffmpeg encoder",
                "pillow"        : "Pillow encoder and decoder",
                "spng"          : "spng codec",
                "jpeg"          : "JPEG codec",
                "vpx"           : "libvpx encoder and decoder",
                "nvjpeg"        : "nvidia nvjpeg hardware encoder",
                "nvenc"         : "nvidia nvenc video hardware encoder",
                "nvdec"         : "nvidia nvdec video hardware decoder",
                "nvfbc"         : "nvidia nvfbc screen capture",
                "x264"          : "libx264 encoder",
                "openh264"      : "openh264 decoder",
                "webp"          : "libwebp encoder and decoder",
                "avif"          : "libavif encoder and decoder",
                "webcam"        : "webcam access",
                "evdi"          : "evdi virtual monitor",
                "drm"           : "direct rendering manager",
                },
    "Pointer" : {
                "mouse"         : "Mouse motion",
                "cursor"        : "Mouse cursor shape",
                },
    "Misc" : {
                #libraries
                "gtk"           : "All GTK code: bindings, client, etc",
                "util"          : "All utility functions",
                "gobject"       : "Command line clients",
                "brotli"        : "Brotli bindings",
                "lz4"           : "LZ4 bindings",
                #server bits:
                "test"          : "Test code",
                "verbose"       : "Very verbose flag",
                #specific applications:
                },
    "Network" : {
                #internal / network:
                "network"       : "All network code",
                "bandwidth"     : "Bandwidth detection and management",
                "ssh"           : "SSH connections",
                "ssl"           : "SSL connections",
                "http"          : "HTTP requests",
                "rfb"           : "RFB Protocol",
                "mmap"          : "mmap transfers",
                "protocol"      : "Packet input and output (formatting, parsing, sending and receiving)",
                "websocket"     : "WebSocket layer",
                "named-pipe"    : "Named pipe",
                "crypto"        : "Encryption",
                "auth"          : "Authentication",
                "upnp"          : "UPnP",
                "quic"          : "QUIC",
                },
    "Server" : {
                #Server:
                "server"        : "All server code",
                "proxy"         : "Proxy server",
                "shadow"        : "Shadow server",
                "command"       : "Server control channel",
                "timeout"       : "Server timeouts",
                "exec"          : "Executing commands",
                #server features:
                "mdns"          : "mDNS session publishing",
                #server internals:
                "stats"         : "Server statistics",
                "xshm"          : "XShm pixel capture",
                },
    "Audio" : {
                "audio"         : "All audio",
                "gstreamer"     : "GStreamer internal messages",
                "av-sync"       : "Audio-video sync",
                },
    "X11" : {
                "x11"           : "All X11 code",
                "xinput"        : "XInput bindings",
                "bindings"      : "X11 Cython bindings",
                "core"          : "X11 core bindings",
                "randr"         : "X11 RandR bindings",
                "ximage"        : "X11 XImage bindings",
                "error"         : "X11 errors",
                },
    "Platform" : {
                "platform"      : "All platform support code",
                "import"        : "Platform support import code",
                "osx"           : "Mac OS X platform support code",
                "win32"         : "Microsoft Windows platform support code",
                "posix"         : "Posix platform code",
                },
    }

#flatten it:
KNOWN_FILTERS : Dict[str,str] = {}
for d in STRUCT_KNOWN_FILTERS.values():
    for k,v in d.items():
        KNOWN_FILTERS[k] = v


def isenvdebug(category : str) -> bool:
    return os.environ.get("XPRA_%s_DEBUG" % category.upper().replace("-", "_").replace("+", "_"), "0")=="1"


def get_info() -> Dict[str,Any]:
    info = {
        "categories" : {
            "enabled"   : tuple(debug_enabled_categories),
            "disabled"  : tuple(debug_disabled_categories),
            },
        "handler"   : getattr(global_logging_handler, "__name__", "<unknown>"),
        "prefix"    : LOG_PREFIX,
        "format"    : LOG_FORMAT,
        "debug-modules" : DEBUG_MODULES,
        #all_loggers
        }
    from xpra.common import FULL_INFO
    if FULL_INFO:
        info["filters"] = STRUCT_KNOWN_FILTERS
    return info


class Logger:
    """
    A wrapper around 'logging' with some convenience stuff.  In particular:
    * You initialize it with a list of categories
        If unset, the default logging target is set to the name of the module where
        Logger() was called.
    * Any of the categories can enable debug logging if the environment
    variable 'XPRA_${CATEGORY}_DEBUG' is set to "1"
    * We also keep a list of debug_categories, so these can get enabled
        programmatically too
    * We keep track of which loggers are associated with each category,
        so we can enable/disable debug logging by category
    * You can pass exc_info=True to any method, and sys.exc_info() will be
        substituted.
    * __call__ is an alias for debug
    * we bypass the logging system unless debugging is enabled for the logger,
        which is much faster than relying on the python logging code
    """
    __slots__ = ("categories", "level", "level_override", "_logger", "debug_enabled", "__weakref__")
    def __init__(self, *categories):
        self.categories = list(categories)
        n = 1
        caller = None
        while n<10:
            try:
                caller = sys._getframe(n).f_globals["__name__"]  # pylint: disable=protected-access
                if caller=="__main__" or caller.startswith("importlib"):
                    n += 1
                else:
                    break
            except (AttributeError, ValueError):
                break
        if caller and caller != "__main__" and not caller.startswith("importlib"):
            self.categories.insert(0, caller)
        self.level = logging.INFO
        self.level_override = 0
        self._logger = logging.getLogger(".".join(self.categories))
        self.setLevel(default_level)
        disabled = False
        enabled = False
        if caller in DEBUG_MODULES:
            enabled = True
        else:
            for cat in self.categories:
                if cat in debug_disabled_categories:
                    disabled = True
                if is_debug_enabled(cat):
                    enabled = True
            if len(categories)>1:
                #try all string permutations of those categories:
                # "keyboard", "events" -> "keyboard+events" or "events+keyboard"
                for cats in itertools.permutations(categories):
                    cstr = "+".join(cats)
                    if cstr in debug_disabled_categories:
                        disabled = True
                    if is_debug_enabled(cstr):
                        enabled = True
        self.debug_enabled = enabled and not disabled
        #ready, keep track of it:
        add_logger(self.categories, self)
        for x in categories:
            if x not in KNOWN_FILTERS:
                self.warn("unknown logging category: %s", x)
        if self.debug_enabled:
            self.debug("debug enabled for %s / %s", caller, categories)

    def get_info(self) -> Dict[str,Any]:
        return {
            "categories"    : self.categories,
            "debug"         : self.debug_enabled,
            "level"         : self._logger.getEffectiveLevel(),
            }

    def __repr__(self):
        return f"Logger{self.categories}"


    def getEffectiveLevel(self) -> int:
        return self._logger.getEffectiveLevel()

    def setLevel(self, level : int) -> None:
        self.level = level
        self._logger.setLevel(level)

    def is_debug_enabled(self) -> bool:
        return self.debug_enabled

    def enable_debug(self):
        self.debug_enabled = True

    def disable_debug(self):
        self.debug_enabled = False

    def critical(self, enable=False):
        self.level_override = logging.CRITICAL if enable else 0

    def log(self, level, msg : str, *args, **kwargs):
        if kwargs.get("exc_info") is True:
            ei = sys.exc_info()
            if ei!=(None, None, None):
                kwargs["exc_info"] = ei
        if LOG_PREFIX:
            msg = LOG_PREFIX+msg
        global_logging_handler(self._logger.log, self.level_override or level, msg, *args, **kwargs)

    def __call__(self, msg : str, *args, **kwargs):
        self.debug(msg, *args, **kwargs)
    def debug(self, msg : str, *args, **kwargs):
        if self.debug_enabled:
            self.log(logging.DEBUG, msg, *args, **kwargs)
    def info(self, msg : str, *args, **kwargs):
        self.log(logging.INFO, msg, *args, **kwargs)
    def warn(self, msg : str, *args, **kwargs):
        self.log(logging.WARN, msg, *args, **kwargs)
    def error(self, msg : str, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs)
    def estr(self, e, **kwargs):
        einfo = str(e) or type(e)
        self.error(f" {einfo}", **kwargs)

    def handle(self, record) -> None:
        self.log(record.levelno, record.msg, *record.args, exc_info=record.exc_info)


# we want to keep a reference to all the loggers in use,
# and we may have multiple loggers for the same key,
# but we don't want to prevent garbage collection so use a list of `weakref`s
all_loggers : Dict[str, Set['weakref.ReferenceType[Logger]']] = {}
def add_logger(categories, logger:Logger) -> None:
    categories = list(categories)
    categories.append("all")
    l = weakref.ref(logger)
    for cat in categories:
        all_loggers.setdefault(cat, set()).add(l)

def get_all_loggers() -> Set[Logger]:
    a = set()
    for loggers_set in all_loggers.values():
        for logger in tuple(loggers_set):
            #weakref:
            instance = logger()
            if instance:
                a.add(instance)
    return a

def get_loggers_for_categories(*cat) -> List[Logger]:
    if not cat:
        return  []
    if "all" in cat:
        return list(get_all_loggers())
    cset = set(cat)
    matches = set()
    for l in get_all_loggers():
        if set(l.categories).issuperset(cset):
            matches.add(l)
    return list(matches)

def enable_debug_for(*cat) -> List[Logger]:
    loggers : List[Logger] = []
    for l in get_loggers_for_categories(*cat):
        if not l.is_debug_enabled():
            l.enable_debug()
            loggers.append(l)
    return loggers

def disable_debug_for(*cat) -> List[Logger]:
    loggers : List[Logger] = []
    for l in get_loggers_for_categories(*cat):
        if l.is_debug_enabled():
            l.disable_debug()
            loggers.append(l)
    return loggers



class CaptureHandler(logging.Handler):
    def __init__(self):
        super().__init__(logging.DEBUG)
        self.records = []

    def handle(self, record):
        self.records.append(record)

    def emit(self, record):
        self.records.append(record)

    def createLock(self):
        self.lock = None

class SIGPIPEStreamHandler(logging.StreamHandler):
    def flush(self):
        try:
            super().flush()
        except BrokenPipeError:
            pass

    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            # issue 35046: merged two stream.writes into one.
            stream.write(msg + self.terminator)
            self.flush()
        except RecursionError:  # See issue 36272
            raise
        except BrokenPipeError:
            pass
        except Exception:
            self.handleError(record)
