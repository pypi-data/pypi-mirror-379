# This file is part of Xpra.
# Copyright (C) 2017-2021 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import socket

def get_interface_info(*_args):
    return {}

def get_tcp_info(_sock):  #pylint: disable=unused-argument
    return {}


from xpra.platform import platform_import
platform_import(globals(), "netdev_query", False,
                "get_tcp_info",
                "get_interface_info",
                )


def print_address(iface, addr, defs):
    from xpra.os_util import POSIX
    from xpra.util import print_nested_dict
    for d in defs:
        ip = d.get("addr")
        if ip:
            stype = {
                socket.AF_INET  : "IPv4",
                socket.AF_INET6 : "IPv6",
                }[addr]
            print(f" * {stype}:     {ip}")
            if POSIX:
                from xpra.net.socket_util import create_tcp_socket
                sock = None
                try:
                    sock = create_tcp_socket(ip, 0)
                    sockfd = sock.fileno()
                    info = get_interface_info(sockfd, iface)
                    if info:
                        print_nested_dict(info, prefix="    ", lchar="-")
                finally:
                    if sock:
                        sock.close()

def print_iface(iface):
    from xpra.os_util import POSIX
    from xpra.net.net_util import import_netifaces
    netifaces = import_netifaces()
    addresses = netifaces.ifaddresses(iface)     #@UndefinedVariable pylint: disable=no-member
    for addr, defs in addresses.items():
        if addr in (socket.AF_INET, socket.AF_INET6):
            print_address(iface, addr, defs)
    if not POSIX:
        info = get_interface_info(0, iface)
        if info:
            print(f"  {info}")

def main():
    # pylint: disable=import-outside-toplevel
    import sys
    from xpra.net.net_util import get_interfaces, if_nametoindex
    from xpra.platform import program_context
    from xpra.log import Logger, enable_color, add_debug_category, enable_debug_for
    log = Logger("network")
    with program_context("Network-Device-Info", "Network Device Info"):
        enable_color()
        verbose = "-v" in sys.argv or "--verbose" in sys.argv
        if verbose:
            enable_debug_for("network")
            add_debug_category("network")
            log.enable_debug()

        print("Network interfaces found:")
        for iface in get_interfaces():
            if if_nametoindex:
                print("* %s (index=%s)" % (iface.ljust(20), if_nametoindex(iface)))
            else:
                print(f"* {iface}")
            print_iface(iface)


if __name__ == "__main__":
    main()
