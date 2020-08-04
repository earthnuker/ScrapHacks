from __future__ import print_function
import frida
import os
import sys
import psutil
import binascii
import sqlite3
import json
import time
import msgpack
from multiprocessing import JoinableQueue
import threading


q = JoinableQueue()


def db_worker(q):
    with open("dump.mp", "wb") as of:
        while True:
            args = q.get()
            if args is None:
                q.task_done()
                break
            msgpack.dump(args, of)
            q.task_done()


db_w = threading.Thread(target=db_worker, args=(q,))

db_w.start()


def on_message(msg, data):
    filename = msg.get("payload", {}).get("filename", "<UNKNOWN>").replace("\\", "/")
    block_id = msg.get("payload", {}).get("block_id", "<UNKNOWN>")
    print(filename,block_id,data)
    msg["payload"]["data"] = data
    q.put(msg["payload"])


def main():
    pid = frida.spawn(sys.argv[1:])
    session = frida.attach(pid)
    script = session.create_script(open("frida_hook_read_trace.js").read())
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


if __name__ == "__main__":
    main()
