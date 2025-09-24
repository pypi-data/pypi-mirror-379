# This file is part of Xpra.
# Copyright (C) 2008, 2009 Nathaniel Smith <njs@pobox.com>
# Copyright (C) 2011-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

from gi.repository import GObject

from xpra.x11.bindings.window import X11WindowBindings #@UnresolvedImport
from xpra.x11.models.core import CoreX11WindowModel
from xpra.log import Logger

log = Logger("x11", "window", "tray")

X11Window = X11WindowBindings()


class TrayGeometryChanged:  # pylint: disable=too-few-public-methods
    __slots__ = ("x", "y", "width", "height")


class SystemTrayWindowModel(CoreX11WindowModel):
    __gproperties__ = CoreX11WindowModel.__common_properties__.copy()
    __gproperties__.update({
        "tray": (GObject.TYPE_BOOLEAN,
                 "Is the window a system tray icon", "",
                 False,
                 GObject.ParamFlags.READABLE),
                })
    __gsignals__ = CoreX11WindowModel.__common_signals__.copy()
    _property_names = CoreX11WindowModel._property_names + ["tray"]
    #these aren't useful, and could actually cause us problems
    _property_names.remove("opaque-region")
    _property_names.remove("protocols")
    _MODELTYPE = "Tray"

    def __init__(self, xid:int, corral_xid:int):
        super().__init__(xid)
        self.corral_xid : int = corral_xid
        self._updateprop("tray", True)

    def __repr__(self) -> str:
        return f"SystemTrayWindowModel({self.xid:x})"

    def _read_initial_X11_properties(self) -> None:
        self._internal_set_property("has-alpha", True)
        super()._read_initial_X11_properties()

    def move_resize(self, x : int, y : int, width : int, height : int) -> None:
        #Used by clients to tell us where the tray is located on screen
        log("SystemTrayModel.move_resize(%s, %s, %s, %s)", x, y, width, height)
        if not X11Window.MoveResizeWindow(self.corral_xid, x, y, width, height):
            return
        X11Window.MoveResizeWindow(self.xid, 0, 0, width, height)
        self._updateprop("geometry", (x, y, width, height))
        #force a refresh:
        event = TrayGeometryChanged()
        event.x = event.y = 0
        event.width , event.height = self.get_dimensions()
        self.emit("client-contents-changed", event)

GObject.type_register(SystemTrayWindowModel)
