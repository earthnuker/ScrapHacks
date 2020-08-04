import frida
import psutil
from binascii import hexlify
import subprocess as SP
import string
import ipaddress
from dissect_net import packet,printable_chars,hexdump,is_printable

def on_message(msg, data=None):
    if not data:
        return
    msg = msg["payload"]
    IP = ipaddress.IPv4Address(msg["addr"])
    IP = ipaddress.IPv4Address(IP.packed[::-1])
    direction = msg["type"]
    port = msg["port"]
    ptr = msg["ptr"]

    with open("netlog.txt","a",encoding="utf8") as of:
        print(
            "{} {}:{} 0x{:x} {}".format(msg["type"], IP, port, ptr, str(hexlify(data),"utf8")),
            file=of
        )
        
    if is_printable(data):
        print(direction, addr, buffer_addr, data)
        return
    
    try:
        parsed_data = packet.parse(data)
        print(
            "{} {}:{} 0x{:x}".format(msg["type"], IP, port, ptr)
        )
        print(hexdump(data))
        print(parsed_data)
        print()
    except Exception as e:
        print(e)
        pass

def main():
    pid = frida.spawn(sys.argv[1:])
    session = frida.attach(pid)
    session.enable_jit()
    script = session.create_script(open("frida_hook_net.js").read())
    open(f"netlog.txt","w",encoding="utf8").close()
    script.on("message", on_message)
    script.load()
    frida.resume(pid)
    proc = psutil.Process(pid)
    proc.wait()
    session.detach()


if __name__ == "__main__":
    main()
