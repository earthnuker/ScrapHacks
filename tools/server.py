import socket
import binascii
import select
from construct import *
from socketserver import BaseRequestHandler,UDPServer

INFO = Struct(
    "version_minor" / Int8ul,
    "version_major" / Int8ul,
    "port" / Int16ul,
    "max_players" / Int16ul,
    "curr_players" / Int16ul,
    "name" / FixedSized(0x20, CString("utf-8")),
    "mode" / FixedSized(0x10, CString("utf-8")),
    "map" / Bytes(2),
    "rest" / GreedyBytes,
)

class ScrapHandler(BaseRequestHandler):
    def handle(self):
        data, socket = self.request
        print(self.client_address,data)
        socket.sendto(data, self.client_address)

class ScrapSrv(UDPServer):
    def __init__(self,port=5000):
        super().__init__(("0.0.0.0",port),ScrapHandler)

with ScrapSrv() as srv:
    srv.serve_forever()

exit()

# sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
    rl, wl, xl = select.select([sock], [sock], [sock], 0.1)
    if rl:
        print(rl)
    for sock in rl:
        data, src = sock.recvfrom(1024)
        print(src, data)
        if data == b"\x7f\x01\x00\x00\x07":
            game_info = INFO.build()
            sock.sendto(game_info, src)
