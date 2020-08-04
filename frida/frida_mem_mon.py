import frida
import sys
import psutil

def on_message(msg, data=None):
    print(msg,data)


def main():
    pid = frida.spawn(sys.argv[1:])
    session = frida.attach(pid)
    session.enable_jit()
    script = session.create_script(open("frida_mem_mon.js").read())
    script.on("message", on_message)
    script.load()
    frida.resume(pid)
    proc = psutil.Process(pid)
    proc.wait()
    session.detach()
    
if __name__ == "__main__":
    main()
