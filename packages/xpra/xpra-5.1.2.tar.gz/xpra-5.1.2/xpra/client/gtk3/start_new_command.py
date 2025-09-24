#!/usr/bin/env python3
# This file is part of Xpra.
# Copyright (C) 2014-2022 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import sys
import gi
gi.require_version("Gtk", "3.0")  # @UndefinedVariable
gi.require_version("Pango", "1.0")  # @UndefinedVariable
gi.require_version("GdkPixbuf", "2.0")  # @UndefinedVariable
from gi.repository import Pango, Gtk  # @UnresolvedImport

from xpra.gtk_common.gtk_util import (
    add_close_accel, scaled_image, get_icon_pixbuf,
    )
from xpra.gtk_common.gobject_compat import register_os_signals
from xpra.util import typedict, net_utf8
from xpra.log import Logger, enable_debug_for

log = Logger("exec")


_instance = None
def getStartNewCommand(run_callback, can_share=False, xdg_menu=None):
    global _instance
    if _instance is None:
        _instance = StartNewCommand(run_callback, can_share, xdg_menu)
    return _instance

def udict(d):
    #with rencode, we may get bytes instead of strings:
    t = typedict()
    for k, v in d.items():
        if isinstance(k, bytes):
            k = net_utf8(k)
        t[k] = v
    return t


class StartNewCommand:

    def __init__(self, run_callback=None, can_share=False, xdg_menu=None):
        self.run_callback = run_callback
        self.xdg_menu = udict(xdg_menu or {})
        self.window = Gtk.Window()
        self.window.set_border_width(20)
        self.window.connect("delete-event", self.close)
        self.window.set_default_size(400, 150)
        self.window.set_title("Start New Command")

        icon_pixbuf = get_icon_pixbuf("forward.png")
        if icon_pixbuf:
            self.window.set_icon(icon_pixbuf)
        self.window.set_position(Gtk.WindowPosition.CENTER)

        vbox = Gtk.VBox(homogeneous=False, spacing=0)
        vbox.set_spacing(0)

        self.entry = Gtk.Entry()
        self.entry.set_max_length(255)
        self.entry.set_width_chars(32)
        self.entry.connect('activate', self.run_command)
        if self.xdg_menu:
            # or use menus if we have xdg data:
            hbox = Gtk.HBox(homogeneous=False, spacing=20)
            vbox.add(hbox)
            hbox.add(Gtk.Label(label="Category:"))
            self.category_combo = Gtk.ComboBoxText()
            hbox.add(self.category_combo)
            for name in sorted(self.xdg_menu.keys()):
                self.category_combo.append_text(name)
            self.category_combo.set_active(0)
            self.category_combo.connect("changed", self.category_changed)

            hbox = Gtk.HBox(homogeneous=False, spacing=20)
            vbox.add(hbox)
            self.command_combo = Gtk.ComboBoxText()
            hbox.pack_start(Gtk.Label(label="Command:"))
            hbox.pack_start(self.command_combo)
            self.command_combo.connect("changed", self.command_changed)
            #this will populate the command combo:
            self.category_changed()
        # always show the command as text so that it can be edited:
        entry_label = Gtk.Label(label="Command to run:")
        entry_label.modify_font(Pango.FontDescription("sans 14"))
        entry_al = Gtk.Alignment(xalign=0, yalign=0.5, xscale=0.0, yscale=0)
        entry_al.add(entry_label)
        vbox.add(entry_al)
        # Actual command:
        vbox.add(self.entry)

        if can_share:
            self.share = Gtk.CheckButton(label="Shared", use_underline=False)
            #Shared commands will also be shown to other clients
            self.share.set_active(True)
            vbox.add(self.share)
        else:
            self.share = None

        # Buttons:
        hbox = Gtk.HBox(homogeneous=False, spacing=20)
        vbox.pack_start(hbox)
        def btn(label, tooltip, callback, icon_name=None):
            btn = Gtk.Button(label=label)
            btn.set_tooltip_text(tooltip)
            btn.connect("clicked", callback)
            icon = get_icon_pixbuf(icon_name)
            if icon:
                btn.set_image(scaled_image(icon, 24))
            hbox.pack_start(btn)
            return btn
        btn("Run", "Run this command", self.run_command, "forward.png")
        btn("Cancel", "", self.close, "quit.png")

        def accel_close(*_args):
            self.close()
        add_close_accel(self.window, accel_close)
        vbox.show_all()
        self.window.vbox = vbox
        self.window.add(vbox)


    def category_changed(self, *args):
        category = self.category_combo.get_active_text()
        entries = udict(udict(self.xdg_menu.dictget(category, {})).dictget("Entries", {}))
        log("category_changed(%s) category=%s, entries=%s", args, category, entries)
        self.command_combo.get_model().clear()
        for name in entries.keys():
            self.command_combo.append_text(name)
        if entries:
            self.command_combo.set_active(0)

    def command_changed(self, *args):
        if not self.entry:
            return
        category = self.category_combo.get_active_text()
        entries = udict(udict(self.xdg_menu.dictget(category, {})).dictget("Entries", {}))
        command_name = self.command_combo.get_active_text()
        log("command_changed(%s) category=%s, entries=%s, command_name=%s", args, category, entries, command_name)
        command = ""
        if entries and command_name:
            command_props = udict(udict(entries).dictget(command_name, {}))
            log("command properties=%s", command_props)
            command = udict(command_props).strget("command", "")
        self.entry.set_text(command)

    def show(self):
        log("show()")
        self.window.show()
        self.window.present()

    def hide(self):
        log("hide()")
        self.window.hide()

    def close(self, *args):
        log("close%s", args)
        self.hide()
        return True

    def destroy(self, *args):
        log("destroy%s", args)
        if self.window:
            self.window.destroy()
            self.window = None

    def run(self):
        log("run()")
        Gtk.main()
        log("run() Gtk.main done")

    def quit(self, *args):
        log("quit%s", args)
        self.close()
        Gtk.main_quit()


    def run_command(self, *_args):
        self.hide()
        command = self.entry.get_text()
        log("command=%s", command)
        if self.run_callback and command:
            self.run_callback(command, self.share is None or self.share.get_active())


def main(): # pragma: no cover
    from xpra.platform.gui import init as gui_init, ready as gui_ready
    from xpra.platform import program_context
    gui_init()
    with program_context("Start-New-Command", "Start New Command"):
        #logging init:
        if "-v" in sys.argv:
            enable_debug_for("util")

        app = StartNewCommand()
        app.hide = app.quit
        register_os_signals(app.quit)
        try:
            gui_ready()
            app.show()
            app.run()
        except KeyboardInterrupt:
            pass
        return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
