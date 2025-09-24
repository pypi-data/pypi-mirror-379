# This file is part of Xpra.
# Copyright (C) 2013-2023 Antoine Martin <antoine@xpra.org>
# Copyright (C) 2008 Nathaniel Smith <njs@pobox.com>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import socket
from time import sleep, time, monotonic
from queue import Queue
from typing import Dict, Any, Callable, Tuple

from xpra.net.net_util import get_network_caps
from xpra.net.compression import Compressed, compressed_wrapper, MIN_COMPRESS_SIZE
from xpra.net.protocol.constants import CONNECTION_LOST
from xpra.net.common import MAX_PACKET_SIZE, PacketType
from xpra.net.digest import get_salt, gendigest
from xpra.codecs.loader import load_codec, get_codec
from xpra.codecs.image_wrapper import ImageWrapper
from xpra.codecs.video_helper import getVideoHelper, PREFERRED_ENCODER_ORDER
from xpra.scripts.config import parse_number, parse_bool
from xpra.common import FULL_INFO
from xpra.os_util import (
    get_hex_uuid, bytestostr, strtobytes,
    )
from xpra.util import (
    flatten_dict, typedict, updict, ellipsizer, envint, envbool,
    csv, first_time, ConnectionMessage,
    )
from xpra.version_util import XPRA_VERSION, vparts
from xpra.make_thread import start_thread
from xpra.server.server_core import get_server_info, get_thread_info, proto_crypto_caps
from xpra.log import Logger

log = Logger("proxy")
enclog = Logger("encoding")


PROXY_QUEUE_SIZE = envint("XPRA_PROXY_QUEUE_SIZE", 0)
#for testing only: passthrough as RGB:
PASSTHROUGH_RGB = envbool("XPRA_PROXY_PASSTHROUGH_RGB", False)
VIDEO_TIMEOUT = 5                  #destroy video encoder after N seconds of idle state
LEGACY_SALT_DIGEST = envbool("XPRA_LEGACY_SALT_DIGEST", False)
PASSTHROUGH_AUTH = envbool("XPRA_PASSTHROUGH_AUTH", True)

PING_INTERVAL = max(1, envint("XPRA_PROXY_PING_INTERVAL", 5))*1000
PING_WARNING = max(5, envint("XPRA_PROXY_PING_WARNING", 5))
PING_TIMEOUT = max(5, envint("XPRA_PROXY_PING_TIMEOUT", 90))

CLIENT_REMOVE_CAPS = ("cipher", "challenge", "digest", "aliases", "compression", "lz4", "lz0", "zlib")
CLIENT_REMOVE_CAPS_CHALLENGE = ("cipher", "digest", "aliases", "compression", "lz4", "lz0", "zlib")


class ProxyInstance:

    def __init__(self, session_options,
                 video_encoder_modules, pings,
                 disp_desc, cipher, cipher_mode, encryption_key, caps):
        self.session_options = session_options
        self.video_encoder_modules = video_encoder_modules
        self.pings = pings
        self.disp_desc = disp_desc
        self.cipher = cipher
        self.cipher_mode = cipher_mode
        self.encryption_key = encryption_key
        self.caps = caps
        log("ProxyInstance%s", (
            session_options,
            video_encoder_modules,
            disp_desc, cipher, cipher_mode, encryption_key,
            "%s: %s.." % (type(caps), ellipsizer(caps))))
        self.uuid = get_hex_uuid()
        self.client_protocol = None
        self.client_has_more = False
        self.server_protocol = None
        self.server_has_more = False
        #ping handling:
        self.client_last_ping = 0
        self.server_last_ping = 0
        self.client_last_ping_echo = 0
        self.server_last_ping_echo = 0
        self.client_last_ping_latency = 0
        self.server_last_ping_latency = 0
        self.client_ping_timer = 0
        self.server_ping_timer = 0
        self.client_challenge_packet = None
        self.exit = False
        self.lost_windows = None
        self.encode_queue = None            #holds draw packets to encode
        self.encode_thread = None
        #setup protocol wrappers:
        self.server_packets : Queue[Tuple] = Queue(PROXY_QUEUE_SIZE)
        self.client_packets : Queue[Tuple] = Queue(PROXY_QUEUE_SIZE)
        self.video_encoding_defs = None
        self.video_encoders = None
        self.video_encoders_last_used_time = None
        self.video_encoder_types = None
        self.video_helper = None

    def is_alive(self) -> bool:
        return not self.exit

    def log_start(self) -> None:
        assert self.client_protocol and self.server_protocol
        log.info("started %s", self)
        log.info(" for client %s", self.client_protocol._conn)
        log.info(" and server %s", self.server_protocol._conn)

    def run(self) -> None:
        self.video_init()

        #server connection tweaks:
        self.server_protocol.large_packets += ["input-devices", "draw", "window-icon",
                                               "keymap-changed", "server-settings"]
        if self.caps.boolget("file-transfer"):
            self.server_protocol.large_packets += ["send-file", "send-file-chunk"]
            self.client_protocol.large_packets += ["send-file", "send-file-chunk"]
        self.server_protocol.set_compression_level(int(self.session_options.get("compression_level", 0)))
        self.server_protocol.enable_default_encoder()

        self.lost_windows = set()
        self.encode_queue = Queue()
        self.encode_thread = start_thread(self.encode_loop, "encode")

        self.start_network_threads()
        if self.caps.boolget("ping-echo-sourceid"):
            self.schedule_client_ping()

        self.send_hello()

    def start_network_threads(self) -> None:
        raise NotImplementedError()


    ################################################################################

    def close_connections(self, skip_proto, *reasons) -> None:
        for proto in (self.client_protocol, self.server_protocol):
            if proto and proto!=skip_proto:
                log("sending disconnect to %s", proto)
                proto.send_disconnect([ConnectionMessage.SERVER_SHUTDOWN]+list(reasons))
        #wait for connections to close down cleanly before we exit
        cp = self.client_protocol
        sp = self.server_protocol
        for i in range(10):
            if cp.is_closed() and sp.is_closed():
                break
            if i==0:
                log("waiting for network connections to close")
            elif i==1:
                log.info("waiting for network connections to close")
            else:
                log("still waiting %i/10 - client.closed=%s, server.closed=%s",
                    i+1, cp.is_closed(), sp.is_closed())
            sleep(0.1)
        if not cp.is_closed():
            log.warn("Warning: proxy instance client connection has not been closed yet:")
            log.warn(" %s", cp)
        if not sp.is_closed():
            log.warn("Warning: proxy instance server connection has not been closed yet:")
            log.warn(" %s", sp)


    def send_disconnect(self, proto, *reasons) -> None:
        log("send_disconnect(%s, %s)", proto, reasons)
        if proto.is_closed():
            return
        proto.send_disconnect(reasons)
        self.timeout_add(1000, self.force_disconnect, proto)

    def force_disconnect(self, proto) -> None:
        proto.close()


    def stop(self, skip_proto, *reasons) -> None:
        log("stop(%s, %s)", skip_proto, reasons)
        if not self.exit:
            log.info("stopping %s", self)
            for x in reasons:
                log.info(" %s", x)
            self.exit = True
        self.cancel_client_ping_timer()
        self.cancel_server_ping_timer()
        self.stop_encode_thread()
        self.close_connections(skip_proto, *reasons)
        self.stopped()

    def stopped(self) -> None:
        pass


    ################################################################################

    def get_proxy_info(self, proto) -> Dict[str,Any]:
        sinfo = {"threads" : get_thread_info(proto)}
        sinfo.update(get_server_info())
        linfo = {}
        if self.client_last_ping_latency:
            linfo["client"] = int(self.client_last_ping_latency)
        if self.server_last_ping_latency:
            linfo["server"] = int(self.server_last_ping_latency)
        return {
            "proxy" : {
                "version"    : vparts(XPRA_VERSION, FULL_INFO+1),
                ""           : sinfo,
                "latency"    : linfo,
                },
            "window" : self.get_window_info(),
            }

    def get_window_info(self) -> Dict[int,Dict[str,Any]]:
        info = {}
        now = monotonic()
        for wid, encoder in self.video_encoders.items():
            einfo = encoder.get_info()
            einfo["idle_time"] = int(now-self.video_encoders_last_used_time.get(wid, 0))
            info[wid] = {
                "proxy"    : {
                    ""           : encoder.get_type(),
                    "encoder"    : einfo
                    },
                }
        enclog("get_window_info()=%s", info)
        return info


    def get_connection_info(self) -> Dict[str,Any]:
        return {
            "client" : self.client_protocol.get_info(),
            "server" : self.server_protocol.get_info(),
            }

    def get_info(self) -> Dict[str,Any]:
        return {"connection" : self.get_connection_info()}


    ################################################################################

    def send_hello(self, challenge_response=None, client_salt=None) -> None:
        hello = self.filter_client_caps(self.caps)
        if challenge_response:
            hello.update({
                "challenge_response"      : challenge_response,
                "challenge_client_salt"   : client_salt,
                })
        self.queue_server_packet(("hello", hello))


    def sanitize_session_options(self, options) -> Dict[str,Any]:
        d = {}
        def number(k, v):
            return parse_number(int, k, v)
        OPTION_WHITELIST : Dict[str,Callable] = {
            "compression_level" : number,
            "lz4"               : parse_bool,
            "zlib"              : parse_bool,
            "rencode"           : parse_bool,
            "rencodeplus"       : parse_bool,
            "bencode"           : parse_bool,
            "yaml"              : parse_bool,
            }
        for k,v in options.items():
            parser = OPTION_WHITELIST.get(k)
            if parser:
                log("trying to add %s=%s using %s", k, v, parser)
                try:
                    d[k] = parser(k, v)
                except Exception as e:
                    log.warn("failed to parse value %s for %s using %s: %s", v, k, parser, e)
        return d

    def filter_client_caps(self, caps, remove=CLIENT_REMOVE_CAPS) -> Dict:
        fc = self.filter_caps(caps, remove, self.server_protocol)
        #the display string may override the username:
        username = self.disp_desc.get("username")
        if username:
            fc["username"] = username
        #update with options provided via config if any:
        fc.update(self.sanitize_session_options(self.session_options))
        #add video proxies if any:
        fc["encoding.proxy.video"] = len(self.video_encoding_defs)>0
        if self.video_encoding_defs:
            fc["encoding.proxy.video.encodings"] = self.video_encoding_defs
        return fc

    def filter_server_caps(self, caps:Dict) -> Dict:
        self.server_protocol.enable_encoder_from_caps(caps)
        return self.filter_caps(caps, ("aliases", ), self.client_protocol)

    def filter_caps(self, caps:Dict, prefixes, proto=None) -> Dict:
        #removes caps that the proxy overrides / does not use:
        pcaps = {}
        removed = []
        for k in caps.keys():
            if any(e for e in prefixes if bytestostr(k).startswith(e)):
                removed.append(k)
            else:
                pcaps[k] = caps[k]
        log("filtered out %s matching %s", removed, prefixes)
        #replace the network caps with the proxy's own:
        ncaps = get_network_caps()
        ncaps.update(proto_crypto_caps(proto))
        pcaps.update(flatten_dict(ncaps))
        #then add the proxy info:
        updict(pcaps, "proxy", get_server_info(), flatten_dicts=True)
        pcaps["proxy"] = True
        pcaps["proxy.hostname"] = socket.gethostname()
        return pcaps


    ################################################################################

    def queue_client_packet(self, packet : PacketType) -> None:
        log("queueing client packet: %s (queue size=%s)", bytestostr(packet[0]), self.client_packets.qsize())
        self.client_packets.put(packet)
        self.client_protocol.source_has_more()

    def get_client_packet(self):
        #server wants a packet
        p = self.client_packets.get()
        s = self.client_packets.qsize()
        log("sending to client: %s (queue size=%i)", bytestostr(p[0]), s)
        return p, None, None, None, True, s>0 or self.server_has_more

    def process_client_packet(self, proto, packet : PacketType) -> None:
        packet_type = bytestostr(packet[0])
        log("process_client_packet: %s", packet_type)
        if packet_type==CONNECTION_LOST:
            self.stop(proto, "client connection lost")
            return
        self.client_has_more = proto.receive_pending
        if packet_type=="set_deflate":
            #echo it back to the client:
            self.client_packets.put(packet)
            self.client_protocol.source_has_more()
            return
        if packet_type=="hello":
            if not self.client_challenge_packet:
                log.warn("Warning: invalid hello packet from client")
                log.warn(" received after initial authentication (dropped)")
                return
            log("forwarding client hello")
            log(" for challenge packet %s", self.client_challenge_packet)
            #update caps with latest hello caps from client:
            self.caps = typedict(packet[1])
            #keep challenge data in the hello response:
            hello = self.filter_client_caps(self.caps, CLIENT_REMOVE_CAPS_CHALLENGE)
            self.queue_server_packet(("hello", hello))
            return
        if packet_type=="ping_echo" and self.client_ping_timer and len(packet)>=7 and strtobytes(packet[6])==strtobytes(self.uuid):
            #this is one of our ping packets:
            self.client_last_ping_echo = packet[1]
            self.client_last_ping_latency = 1000*monotonic()-self.client_last_ping_echo
            log("ping-echo: client latency=%.1fms", self.client_last_ping_latency)
            return
        #the packet types below are forwarded:
        if packet_type=="disconnect":
            reasons = tuple(bytestostr(x) for x in packet[1:])
            log("got disconnect from client: %s", csv(reasons))
            if self.exit:
                self.client_protocol.close()
            else:
                self.stop(None, "disconnect from client", *reasons)
        elif packet_type=="send-file" and packet[6]:
            packet = self.compressed_marker(packet, 6,"file-data")
        elif packet_type=="send-file-chunk" and packet[3]:
            packet = self.compressed_marker(packet, 3, "file-chunk-data")
        self.queue_server_packet(packet)

    def compressed_marker(self, packet : PacketType, index:int, description:str):
        return self.replace_packet_item(packet, index, Compressed(description, packet[index], can_inline=False))

    def replace_packet_item(self, packet : PacketType, index:int, new_value:Any) -> PacketType:
        # make the packet data mutable and replace the contents at `index`:
        assert index>0
        lpacket = list(packet)
        lpacket[index] = new_value
        # noinspection PyTypeChecker
        return tuple(lpacket)

    def queue_server_packet(self, packet : PacketType) -> None:
        log("queueing server packet: %s (queue size=%s)", bytestostr(packet[0]), self.server_packets.qsize())
        self.server_packets.put(packet)
        self.server_protocol.source_has_more()

    def get_server_packet(self):
        #server wants a packet
        p = self.server_packets.get()
        s = self.server_packets.qsize()
        log("sending to server: %s (queue size=%i)", bytestostr(p[0]), s)
        return p, None, None, None, True, s>0 or self.client_has_more


    def _packet_recompress(self, packet : PacketType, index:int, name:str) -> PacketType:
        if len(packet)<=index:
            return packet
        data = packet[index]
        if len(data)<MIN_COMPRESS_SIZE:
            return packet
        #this is ugly and not generic!
        kw = dict((k, self.caps.boolget(k)) for k in ("zlib", "lz4"))
        return self.replace_packet_item(packet, index, compressed_wrapper(name, data, can_inline=False, **kw))


    def cancel_server_ping_timer(self) -> None:
        spt = self.server_ping_timer
        log("cancel_server_ping_timer() server_ping_timer=%s", spt)
        if spt:
            self.server_ping_timer = 0
            self.source_remove(spt)

    def cancel_client_ping_timer(self) -> None:
        cpt = self.client_ping_timer
        log("cancel_client_ping_timer() client_ping_timer=%s", cpt)
        if cpt:
            self.client_ping_timer = 0
            self.source_remove(cpt)

    def schedule_server_ping(self) -> None:
        log("schedule_server_ping()")
        self.cancel_server_ping_timer()
        self.server_last_ping_echo = monotonic()
        self.server_ping_timer = self.timeout_add(PING_INTERVAL, self.send_server_ping)

    def schedule_client_ping(self) -> None:
        log("schedule_client_ping()")
        self.cancel_client_ping_timer()
        self.client_last_ping_echo = monotonic()
        self.client_ping_timer = self.timeout_add(PING_INTERVAL, self.send_client_ping)

    def send_server_ping(self) -> bool:
        log("send_server_ping() server_last_ping=%s", self.server_last_ping)
        #if we've already sent one, check for the echo:
        if self.server_last_ping:
            delta = self.server_last_ping-self.server_last_ping_echo
            if delta>PING_WARNING:
                log.warn("Warning: late server ping, %i seconds", delta)
            if delta>PING_TIMEOUT:
                log.error("Error: server ping timeout, %i seconds", delta)
                self.stop(None, "proxy to server ping timeout")
                return False
        now = monotonic()
        self.server_last_ping = now
        packet : PacketType = ("ping", int(now*1000), int(time()*1000), self.uuid)
        self.queue_server_packet(packet)
        return True

    def send_client_ping(self) -> bool:
        log("send_client_ping() client_last_ping=%s", self.client_last_ping)
        #if we've already sent one, check for the echo:
        if self.client_last_ping:
            delta = self.client_last_ping-self.client_last_ping_echo
            if delta>PING_WARNING:
                log.warn("Warning: late client ping, %i seconds", delta)
            if delta>PING_TIMEOUT:
                log.error("Error: client ping timeout, %i seconds", delta)
                self.stop(None, "proxy to client ping timeout")
                return False
        now = monotonic()
        self.client_last_ping = now
        packet : PacketType = ("ping", int(now*1000), int(time()*1000), self.uuid)
        self.queue_client_packet(packet)
        return True


    def process_server_packet(self, proto, packet : PacketType) -> None:
        packet_type = bytestostr(packet[0])
        log("process_server_packet: %s", packet_type)
        if packet_type==CONNECTION_LOST:
            self.stop(proto, "server connection lost")
            return
        self.server_has_more = proto.receive_pending
        if packet_type=="disconnect":
            reason = bytestostr(packet[1])
            log("got disconnect from server: %s", reason)
            if self.exit:
                self.server_protocol.close()
            else:
                self.stop(None, "disconnect from server", reason)
        elif packet_type=="hello":
            c = typedict(packet[1])
            if c.boolget("ping-echo-sourceid"):
                self.schedule_server_ping()
            maxw, maxh = c.intpair("max_desktop_size", (4096, 4096))
            caps = self.filter_server_caps(c)
            #add new encryption caps:
            if self.cipher:
                from xpra.net.crypto import crypto_backend_init, new_cipher_caps, DEFAULT_PADDING   # pylint: disable=import-outside-toplevel
                crypto_backend_init()
                enc_caps = self.caps.dictget("encryption")
                padding_options = typedict(enc_caps or {}).strtupleget("padding.options", [DEFAULT_PADDING])
                auth_caps = new_cipher_caps(self.client_protocol,
                                            self.cipher, self.cipher_mode, self.encryption_key, padding_options)
                caps.update(auth_caps)
            #may need to bump packet size:
            proto.max_packet_size = max(MAX_PACKET_SIZE, maxw*maxh*4*4)
            packet = ("hello", caps)
        elif packet_type=="ping_echo" and self.server_ping_timer and len(packet)>=7 and strtobytes(packet[6])==strtobytes(self.uuid):
            #this is one of our ping packets:
            self.server_last_ping_echo = packet[1]
            self.server_last_ping_latency = 1000*monotonic()-self.server_last_ping_echo
            log("ping-echo: server latency=%.1fms", self.server_last_ping_latency)
            return
        elif packet_type=="info-response":
            #adds proxy info:
            #note: this is only seen by the client application
            #"xpra info" is a new connection, which talks to the proxy server...
            info = packet[1]
            info.update(self.get_proxy_info(proto))
        elif packet_type=="lost-window":
            wid = packet[1]
            #mark it as lost, so we can drop any current/pending frames
            self.lost_windows.add(wid)
            #queue it so it gets cleaned safely (for video encoders mostly):
            self.encode_queue.put(packet)
            #and fall through so tell the client immediately
        elif packet_type=="draw":
            #use encoder thread:
            self.encode_queue.put(packet)
            #which will queue the packet itself when done:
            return
        elif packet_type=="sound-data":
            if packet[2]:
                #best if we use raw packets for the actual sound-data chunk:
                packet = self.compressed_marker(packet, 2, "sound-data")
        #we do want to reformat cursor packets...
        #as they will have been uncompressed by the network layer already:
        elif packet_type=="cursor":
            #packet = ["cursor", "png", x, y, width, height, xhot, yhot, serial, pixels, name]
            #or:
            #packet = ["cursor", ""]
            if len(packet)>=8:
                packet = self._packet_recompress(packet, 9, "cursor")
        elif packet_type=="window-icon":
            if not isinstance(packet[5], str):
                packet = self._packet_recompress(packet, 5, "icon")
        elif packet_type=="send-file":
            if packet[6]:
                packet = self.compressed_marker(packet, 6, "file-data")
        elif packet_type=="send-file-chunk":
            if packet[3]:
                packet = self.compressed_marker(packet, 3, "file-chunk-data")
        elif packet_type=="challenge":
            password = self.disp_desc.get("password", self.session_options.get("password"))
            log("password from %s / %s = %s", self.disp_desc, self.session_options, password)
            if not password:
                if not PASSTHROUGH_AUTH:
                    self.stop(None, "authentication requested by the server,",
                              "but no password is available for this session")
                #otherwise, just forward it to the client
                self.client_challenge_packet = packet
            else:
                #client may have already responded to the challenge,
                #so we have to handle authentication from this end
                server_salt = strtobytes(packet[1])
                l = len(server_salt)
                digest = bytestostr(packet[3])
                salt_digest = "xor"
                if len(packet)>=5:
                    salt_digest = bytestostr(packet[4])
                if salt_digest in ("xor", "des"):
                    if not LEGACY_SALT_DIGEST:
                        self.stop(None, f"server uses legacy salt digest {salt_digest!r}")
                        return
                    log.warn("Warning: server using legacy support for '%s' salt digest", salt_digest)
                if salt_digest=="xor":
                    #with xor, we have to match the size
                    if l<16:
                        raise ValueError(f"server salt is too short: only {l} bytes, minimum is 16")
                    if l>256:
                        raise ValueError(f"server salt is too long: {l} bytes, maximum is 256")
                else:
                    #other digest, 32 random bytes is enough:
                    l = 32
                client_salt = get_salt(l)
                salt = gendigest(salt_digest, client_salt, server_salt)
                challenge_response = gendigest(digest, password, salt)
                if not challenge_response:
                    log("invalid digest module '%s': %s", digest)
                    self.stop(None, f"server requested {digest!r} digest but it is not supported")
                    return
                log.info("sending %s challenge response", digest)
                self.send_hello(challenge_response, client_salt)
                return
        self.queue_client_packet(packet)


    def stop_encode_thread(self) -> None:
        #empty the encode queue:
        q = self.encode_queue
        if q:
            q.put_nowait(None)
            q = Queue()
            q.put(None)
            self.encode_queue = q

    def encode_loop(self) -> None:
        """ thread for slower encoding related work """
        def delvideo(wid:int):
            self.video_encoders.pop(wid, None)
            self.video_encoders_last_used_time.pop(wid, None)
        while not self.exit:
            packet = self.encode_queue.get()
            if packet is None:
                return
            try:
                packet_type = bytestostr(packet[0])
                if packet_type=="lost-window":
                    wid = packet[1]
                    self.lost_windows.remove(wid)
                    ve = self.video_encoders.get(wid)
                    if ve:
                        delvideo(wid)
                        ve.clean()
                elif packet_type=="draw":
                    #modify the packet with the video encoder:
                    self.process_draw(packet)
                elif packet_type=="check-video-timeout":
                    #not a real packet, this is added by the timeout check:
                    wid = packet[1]
                    ve = self.video_encoders.get(wid)
                    now = monotonic()
                    idle_time = now-self.video_encoders_last_used_time.get(wid, 0)
                    if ve and idle_time>VIDEO_TIMEOUT:
                        enclog("timing out the video encoder context for window %s", wid)
                        #timeout is confirmed, we are in the encoding thread,
                        #so it is now safe to clean it up:
                        ve.clean()
                        delvideo(wid)
                else:
                    enclog.warn("unexpected encode packet: %s", packet_type)
            except Exception:
                enclog.warn("error encoding packet", exc_info=True)


    def process_draw(self, packet : PacketType) -> bool:
        wid, x, y, width, height, encoding, pixels, _, rowstride, client_options = packet[1:11]
        encoding = bytestostr(encoding)
        #never modify mmap or scroll packets:
        if encoding in ("mmap", "scroll"):
            self.queue_client_packet(packet)
            return
        #we can only use video encoders on RGB data:
        if encoding not in ("rgb24", "rgb32", "r210", "BGR565"):
            #this prevents compression and inlining of pixel data:
            packet = self.compressed_marker(packet, 7, f"{encoding} pixels")
            self.queue_client_packet(packet)
            return
        client_options = typedict(client_options)
        #we have a proxy video packet:
        rgb_format = client_options.strget("rgb_format", "")
        enclog("proxy draw: encoding=%s, client_options=%s", encoding, client_options)

        def send_updated(packet:PacketType, encoding, compressed_data, updated_client_options) -> bool:
            #update the packet with actual encoding data used:
            packet = self.replace_packet_item(packet, 6, encoding)
            packet = self.replace_packet_item(packet, 7, compressed_data)
            packet = self.replace_packet_item(packet, 10, updated_client_options)
            enclog("returning %s bytes from %s, options=%s", len(compressed_data), len(pixels), updated_client_options)
            if wid not in self.lost_windows:
                self.queue_client_packet(packet)

        def passthrough(strip_alpha=True) -> None:
            enclog("proxy draw: %s passthrough (rowstride: %s vs %s, strip alpha=%s)",
                   rgb_format, rowstride, client_options.intget("rowstride", 0), strip_alpha)
            updated = packet
            if strip_alpha:
                #passthrough as plain RGB:
                Xindex = rgb_format.upper().find("X")
                if Xindex>=0 and len(rgb_format)==4:
                    #force clear alpha (which may be garbage):
                    newdata = bytearray(pixels)
                    c = 255
                    for i in range(len(pixels)//4):
                        newdata[i*4+Xindex] = c
                    updated = self.replace_packet_item(packet, 9, client_options.intget("rowstride", 0))
                    cdata = bytes(newdata)
                else:
                    cdata = pixels
                new_client_options = {"rgb_format" : rgb_format}
            else:
                #preserve
                cdata = pixels
                new_client_options = client_options
            wrapped = Compressed(f"{encoding} pixels", cdata)
            #rgb32 is always supported by all clients:
            send_updated(updated, encoding, wrapped, new_client_options)

        proxy_video = client_options.boolget("proxy", False)
        if PASSTHROUGH_RGB:
            #we are dealing with rgb data, so we can pass it through:
            passthrough(proxy_video)
            return
        if not self.video_encoder_types or not client_options or not proxy_video:
            #ensure we don't try to re-compress the pixel data in the network layer:
            #(re-add the "compressed" marker that gets lost when we re-assemble packets)
            packet = self.compressed_marker(packet, 7, f"{encoding} pixels")
            self.queue_client_packet(packet)
            return

        #video encoding: find existing encoder
        ve = self.video_encoders.get(wid)
        if ve:
            if ve in self.lost_windows:
                #we cannot clean the video encoder here, there may be more frames queue up
                #"lost-window" in encode_loop will take care of it safely
                return
            #we must verify that the encoder is still valid
            #and scrap it if not (ie: when window is resized)
            if ve.get_width()!=width or ve.get_height()!=height:
                enclog("closing existing video encoder %s because dimensions have changed from %sx%s to %sx%s",
                       ve, ve.get_width(), ve.get_height(), width, height)
                ve.clean()
                ve = None
            elif ve.get_encoding()!=encoding:
                enclog("closing existing video encoder %s because encoding has changed from %s to %s",
                       ve.get_encoding(), encoding)
                ve.clean()
                ve = None
        #scaling and depth are proxy-encoder attributes:
        scaling = client_options.inttupleget("scaling", (1, 1))
        depth   = client_options.intget("depth", 24)
        rowstride = client_options.intget("rowstride", rowstride)
        quality = client_options.intget("quality", -1)
        speed   = client_options.intget("speed", -1)
        timestamp = client_options.intget("timestamp")

        image = ImageWrapper(x, y, width, height, pixels, rgb_format, depth, rowstride, planes=ImageWrapper.PACKED)
        if timestamp is not None:
            image.set_timestamp(timestamp)

        #the encoder options are passed through:
        encoder_options = client_options.dictget("options", {})
        if not ve:
            #make a new video encoder:
            spec = self._find_video_encoder(encoding, rgb_format)
            if spec is None:
                #no video encoder!
                enc_pillow = get_codec("enc_pillow")
                if not enc_pillow:
                    if first_time(f"no-video-no-PIL-{rgb_format}"):
                        enclog.warn("Warning: no video encoder found for rgb format %s", rgb_format)
                        enclog.warn(" sending as plain RGB")
                    passthrough(True)
                    return
                enclog("no video encoder available: sending as jpeg")
                coding, compressed_data, client_options = enc_pillow.encode("jpeg", image, quality, speed, False)[:3]
                send_updated(packet, coding, compressed_data, client_options)
                return

            enclog("creating new video encoder %s for window %s", spec, wid)
            ve = spec.make_instance()
            #dst_formats is specified with first frame only:
            dst_formats = client_options.strtupleget("dst_formats")
            if dst_formats is not None:
                #save it in case we time out the video encoder,
                #so we can instantiate it again, even from a frame no>1
                self.video_encoders_dst_formats = dst_formats
            else:
                if not self.video_encoders_dst_formats:
                    raise ValueError("BUG: dst_formats not specified for proxy and we don't have it either")
                dst_formats = self.video_encoders_dst_formats
            ve.init_context(width, height, rgb_format, dst_formats, encoding, quality, speed, scaling, {})
            self.video_encoders[wid] = ve
            self.video_encoders_last_used_time[wid] = monotonic()      #just to make sure this is always set
        #actual video compression:
        enclog("proxy compression using %s with quality=%s, speed=%s", ve, quality, speed)
        if quality > 0:
            encoder_options["quality"] = quality
        if speed > 0:
            encoder_options["speed"] = speed
        data, out_options = ve.compress_image(image, encoder_options)
        #pass through some options if we don't have them from the encoder
        #(maybe we should also use the "pts" from the real server?)
        for k in ("timestamp", "rgb_format", "depth", "csc"):
            if k not in out_options and k in client_options:
                out_options[k] = client_options[k]
        self.video_encoders_last_used_time[wid] = monotonic()
        send_updated(packet, ve.get_encoding(), Compressed(encoding, data), out_options)

    def timeout_video_encoders(self) -> bool:
        #have to be careful as another thread may come in...
        #so we just ask the encode thread (which deals with encoders already)
        #to do what may need to be done if we find a timeout:
        now = monotonic()
        for wid in tuple(self.video_encoders_last_used_time.keys()):
            vetime = self.video_encoders_last_used_time.get(wid)
            if not vetime:
                continue
            idle_time = int(now-vetime)
            enclog("timeout_video_encoders() wid=%s, idle_time=%s", wid, idle_time)
            if idle_time and idle_time>VIDEO_TIMEOUT:
                self.encode_queue.put(["check-video-timeout", wid])
        return True     #run again

    def _find_video_encoder(self, video_encoding, rgb_format):
        #try the one specified first, then all the others:
        try_encodings = [video_encoding] + [x for x in self.video_helper.get_encodings() if x!=video_encoding]
        for encoding in try_encodings:
            colorspace_specs = self.video_helper.get_encoder_specs(encoding)
            especs = colorspace_specs.get(rgb_format)
            if not especs:
                continue
            for etype in self.video_encoder_types:
                for spec in especs:
                    if etype==spec.codec_type:
                        enclog("_find_video_encoder(%s, %s)=%s", encoding, rgb_format, spec)
                        return spec
        enclog("_find_video_encoder(%s, %s) not found", video_encoding, rgb_format)
        return None

    def video_helper_init(self) -> None:
        self.video_helper = getVideoHelper()
        #only use video encoders (no CSC supported in proxy)
        self.video_helper.set_modules(video_encoders=self.video_encoder_modules)
        self.video_helper.init()

    def video_init(self) -> None:
        enclog("video_init() loading codecs")
        enclog("video_init() loading pillow encoder")
        load_codec("enc_pillow")
        enclog("video_init() will try video encoders: %s", csv(self.video_encoder_modules) or "none")
        self.video_helper_init()

        self.video_encoding_defs = {}
        self.video_encoders = {}
        self.video_encoders_dst_formats = []
        self.video_encoders_last_used_time = {}
        self.video_encoder_types = []

        #figure out which encoders we want to proxy for (if any):
        encoder_types = set()
        for encoding in self.video_helper.get_encodings():
            colorspace_specs = self.video_helper.get_encoder_specs(encoding)
            for colorspace, especs in colorspace_specs.items():
                if colorspace not in ("BGRX", "BGRA", "RGBX", "RGBA"):
                    #only deal with encoders that can handle plain RGB directly
                    continue

                for spec in especs:                             #ie: video_spec("x264")
                    spec_props = spec.to_dict()
                    del spec_props["codec_class"]               #not serializable!
                    #we want to win scoring, so we get used ahead of other encoders:
                    spec_props["score_boost"] = 50
                    #limit to 3 video streams we proxy for (we really want 2,
                    # but because of races with garbage collection, we need to allow more)
                    spec_props["max_instances"] = 3

                    #store it in encoding defs:
                    self.video_encoding_defs.setdefault(encoding, {}).setdefault(colorspace, []).append(spec_props)
                    encoder_types.add(spec.codec_type)

        enclog("encoder types found: %s", tuple(encoder_types))
        #remove duplicates and use preferred order:
        order = list(PREFERRED_ENCODER_ORDER)
        for x in tuple(encoder_types):
            if x not in order:
                order.append(x)
        self.video_encoder_types = [x for x in order if x in encoder_types]
        enclog.info("proxy video encoders: %s", csv(self.video_encoder_types or ["none",]))
        self.timeout_add(VIDEO_TIMEOUT*1000, self.timeout_video_encoders)
