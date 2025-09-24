# This file is part of Xpra.
# Copyright (C) 2010-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.
#pylint: disable-msg=E1101

from time import monotonic
from typing import Tuple, Dict, Callable

from xpra.common import noop
from xpra.util import envint, AtomicInteger, typedict
from xpra.net.common import PacketType
from xpra.client.base.stub_client_mixin import StubClientMixin
from xpra.log import Logger

log = Logger("client", "rpc")

RPC_TIMEOUT = envint("XPRA_RPC_TIMEOUT", 5000)


class RPCClient(StubClientMixin):
    """
    Utility mixin for client classes that handle RPC calls
    """

    def __init__(self):
        super().__init__()
        #rpc / dbus:
        self.rpc_counter = AtomicInteger()
        self.server_dbus_proxy = False
        self.server_rpc_types : Tuple[str,...] = ()
        self.rpc_filter_timers : Dict[int,int] = {}
        self.rpc_pending_requests : Dict[int,Tuple[float, str, Tuple, Callable, Callable]] = {}

    def cleanup(self):
        timers = tuple(self.rpc_filter_timers.values())
        self.rpc_filter_timers = {}
        for t in timers:
            self.source_remove(t)


    def parse_server_capabilities(self, c : typedict) -> bool:
        self.server_dbus_proxy = c.boolget("dbus_proxy")
        #default for pre-0.16 servers:
        default_rpc_types : Tuple[str,...] = ()
        if self.server_dbus_proxy:
            default_rpc_types = ("dbus", )
        self.server_rpc_types = c.strtupleget("rpc-types", default_rpc_types)
        return True


    def rpc_call(self, rpc_type:str, rpc_args, reply_handler:Callable=noop, error_handler:Callable=noop) -> None:
        assert rpc_type in self.server_rpc_types, "server does not support %s rpc" % rpc_type
        rpcid = self.rpc_counter.increase()
        self.rpc_filter_pending(rpcid)
        #keep track of this request (for timeout / error and reply callbacks):
        req = monotonic(), rpc_type, rpc_args, reply_handler, error_handler
        self.rpc_pending_requests[rpcid] = req
        log("sending %s rpc request %s to server: %s", rpc_type, rpcid, req)
        packet = ["rpc", rpc_type, rpcid] + rpc_args
        self.send(*packet)
        self.rpc_filter_timers[rpcid] = self.timeout_add(RPC_TIMEOUT, self.rpc_filter_pending, rpcid)

    def rpc_filter_pending(self, rpcid:int) -> None:
        """ removes timed out dbus requests """
        del self.rpc_filter_timers[rpcid]
        for k in tuple(self.rpc_pending_requests.keys()):
            v = self.rpc_pending_requests.get(k)
            if v is None:
                continue
            t, rpc_type, rpc_args, reply_handler, ecb = v
            if 1000*(monotonic()-t)>=RPC_TIMEOUT:
                log.warn("Warning: %s rpc request: %s has timed out", rpc_type, reply_handler)
                log.warn(" args: %s", rpc_args)
                try:
                    del self.rpc_pending_requests[k]
                    if ecb is not None:
                        ecb("timeout")
                except Exception as e:
                    log.error("Error during timeout handler for %s rpc callback:", rpc_type)
                    log.estr(e)
                    del e


    ######################################################################
    #packet handlers
    def _process_rpc_reply(self, packet : PacketType) -> None:
        rpc_type, rpcid, success, args = packet[1:5]
        log("rpc_reply: %s", (rpc_type, rpcid, success, args))
        v = self.rpc_pending_requests.get(rpcid)
        assert v is not None, "pending dbus handler not found for id %s" % rpcid
        assert rpc_type==v[1], "rpc reply type does not match: expected %s got %s" % (v[1], rpc_type)
        del self.rpc_pending_requests[rpcid]
        if success:
            ctype = "ok"
            rh = v[-2]      #ok callback
        else:
            ctype = "error"
            rh = v[-1]      #error callback
        if rh is None:
            log("no %s rpc callback defined, return values=%s", ctype, args)
            return
        log("calling %s callback %s(%s)", ctype, rh, args)
        try:
            rh(*args)
        except Exception as e:
            log.error("Error processing rpc reply handler %s(%s) :", rh, args)
            log.estr(e)


    def init_authenticated_packet_handlers(self) -> None:
        log("init_authenticated_packet_handlers()")
        self.add_packet_handler("rpc-reply", self._process_rpc_reply)
