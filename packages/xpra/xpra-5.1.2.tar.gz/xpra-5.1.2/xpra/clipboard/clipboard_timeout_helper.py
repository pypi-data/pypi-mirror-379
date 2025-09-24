# This file is part of Xpra.
# Copyright (C) 2019-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

from typing import Dict, Tuple, Optional, List, Any

from gi.repository import GLib  # @UnresolvedImport

from xpra.clipboard.clipboard_core import ClipboardProtocolHelperCore, ClipboardProxyCore
from xpra.util import repr_ellipsized, ellipsizer, envint, engs
from xpra.log import Logger
from xpra.platform.features import CLIPBOARD_GREEDY

log = Logger("clipboard")

CONVERT_TIMEOUT = envint("XPRA_CLIPBOARD_CONVERT_TIMEOUT", 100)
if not 0<CONVERT_TIMEOUT<=5000:
    log.warn("Warning: invalid value for 'XPRA_CLIPBOARD_CONVERT_TIMEOUT'")
    CONVERT_TIMEOUT = max(0, min(5000, CONVERT_TIMEOUT))
REMOTE_TIMEOUT = envint("XPRA_CLIPBOARD_REMOTE_TIMEOUT", 2500)
if not 0<REMOTE_TIMEOUT<=5000:
    log.warn("Warning: invalid value for 'XPRA_CLIPBOARD_REMOTE_TIMEOUT'")
    REMOTE_TIMEOUT = max(0, min(5000, REMOTE_TIMEOUT))


class ClipboardTimeoutHelper(ClipboardProtocolHelperCore):

    #a clipboard superclass that handles timeouts
    def __init__(self, send_packet_cb, progress_cb=None, **kwargs):
        super().__init__(send_packet_cb, progress_cb, **kwargs)
        self._clipboard_outstanding_requests : Dict[int, Tuple[int,str,str]] = {}

    def cleanup(self) -> None:
        #reply to outstanding requests with "no data":
        for request_id in tuple(self._clipboard_outstanding_requests.keys()):
            self._clipboard_got_contents(request_id)
        self._clipboard_outstanding_requests = {}
        super().cleanup()

    def make_proxy(self, selection:str):
        raise NotImplementedError()

    def _get_proxy(self, selection:str) -> Optional[ClipboardProxyCore]:
        proxy = self._clipboard_proxies.get(selection)
        if not proxy:
            log.warn("Warning: no clipboard proxy for '%s'", selection)
            return None
        return proxy

    def set_want_targets_client(self, want_targets:bool) -> None:
        super().set_want_targets_client(want_targets)
        #pass it on to the ClipboardProxy instances:
        for proxy in self._clipboard_proxies.values():
            proxy.set_want_targets(want_targets)


    ############################################################################
    # network methods for communicating with the remote clipboard:
    ############################################################################
    def _send_clipboard_token_handler(self, proxy : ClipboardProxyCore, packet_data=()):
        if log.is_debug_enabled():
            log("_send_clipboard_token_handler(%s, %s)", proxy, repr_ellipsized(packet_data))
        remote = self.local_to_remote(proxy._selection)
        packet : List[Any] = ["clipboard-token", remote]
        if packet_data:
            #append 'TARGETS' unchanged:
            packet.append(packet_data[0])
            #if present, the next element is the target data,
            #which we have to convert to wire format:
            if len(packet_data)>=2:
                target, dtype, dformat, data = packet_data[1]
                wire_encoding, wire_data = self._munge_raw_selection_to_wire(target, dtype, dformat, data)
                if wire_encoding:
                    wire_data = self._may_compress(dtype, dformat, wire_data)
                    if wire_data:
                        packet += [target, dtype, dformat, wire_encoding, wire_data]
                        claim = proxy._can_send
                        packet += [claim, CLIPBOARD_GREEDY]
        log("send_clipboard_token_handler %s to %s", proxy._selection, remote)
        self.send(*packet)

    def _send_clipboard_request_handler(self, proxy:ClipboardProxyCore, selection:str, target:str):
        log("send_clipboard_request_handler%s", (proxy, selection, target))
        request_id = self._clipboard_request_counter
        self._clipboard_request_counter += 1
        remote = self.local_to_remote(selection)
        log("send_clipboard_request %s to %s, id=%s", selection, remote, request_id)
        timer = GLib.timeout_add(REMOTE_TIMEOUT, self.timeout_request, request_id)
        self._clipboard_outstanding_requests[request_id] = (timer, selection, target)
        self.progress()
        self.send("clipboard-request", request_id, remote, target)

    def timeout_request(self, request_id:int) -> None:
        try:
            selection, target = self._clipboard_outstanding_requests.pop(request_id)[1:]
        except KeyError:
            log.warn("Warning: clipboard request id %i not found", request_id)
            return
        finally:
            self.progress()
        log.warn("Warning: remote clipboard request timed out")
        log.warn(" request id %i, selection=%s, target=%s", request_id, selection, target)
        proxy = self._get_proxy(selection)
        if proxy:
            proxy.got_contents(target)

    def _clipboard_got_contents(self, request_id:int, dtype:str="", dformat:int=0, data=None) -> None:
        try:
            timer, selection, target = self._clipboard_outstanding_requests.pop(request_id)
        except KeyError:
            log.warn("Warning: request id %i not found", request_id)
            log.warn(" already timed out or duplicate reply")
            return
        finally:
            self.progress()
        GLib.source_remove(timer)
        proxy = self._get_proxy(selection)
        log("clipboard got contents%s: proxy=%s for selection=%s",
            (request_id, dtype, dformat, ellipsizer(data)), proxy, selection)
        if data and isinstance(data, memoryview):
            data = bytes(data)
        if proxy:
            proxy.got_contents(target, dtype, dformat, data)

    def client_reset(self) -> None:
        super().client_reset()
        #timeout all pending requests
        cor = self._clipboard_outstanding_requests
        if cor:
            log.info("cancelling %i clipboard request%s", len(cor), engs(cor))
            self._clipboard_outstanding_requests = {}
            for request_id in cor:
                self._clipboard_got_contents(request_id)
