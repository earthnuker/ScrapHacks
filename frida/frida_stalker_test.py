import frida
import sys
import psutil
import subprocess as SP
import threading
from multiprocessing import JoinableQueue
import msgpack


q = JoinableQueue()


def db_worker(q):
    events = 0
    with open("trace.mp", "wb") as of:
        while True:
            args = q.get()
            if args is None:
                q.task_done()
                break
            events += 1
            msgpack.dump(args, of)
            q.task_done()
    print("Wrote", events, "events")


db_w = threading.Thread(target=db_worker, args=(q,))

db_w.start()
modules = {}
mem_range = None


def on_message(msg, data=None):
    global mem_range
    data = msg["payload"]
    if "stalker" in data:
        for val in data["stalker"]:
            q.put(val)


def main():
    pid = frida.spawn(sys.argv[1:])
    session = frida.attach(pid)
    session.enable_jit()
    script = session.create_script(open("frida_stalker_test.js").read())
    script.on("message", on_message)
    script.load()
    frida.resume(pid)
    proc = psutil.Process(pid)
    proc.wait()
    session.detach()
    q.put(None)
    q.join()
    q.close()
    db_w.join()


"""
import msgpack as mp
from collections import Counter
data=list(mp.Unpacker(open("trace.mp","rb"), raw=False))
Counter(v[1] for v in data).most_common(10)
"""

if __name__ == "__main__":
    main()
