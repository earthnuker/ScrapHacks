var sendto = Module.getExportByName("WSOCK32.dll", "sendto")
var recvfrom = Module.getExportByName("WSOCK32.dll", "recvfrom")

Interceptor.attach(ptr("0x004f9300"), {
    onEnter: function (args) {
        console.log("[SendUsrString]", JSON.stringify({
            data: args[0].readCString(),
            dst: args[1].toInt32(),
            chat: args[2].toInt32()
        }));
    }
})

Interceptor.attach(ptr(sendto), {
    onEnter: function (args) {
        this.socket = args[0];
        this.buffer = args[1];
        this.size = args[2].toInt32();
        this.flags = args[3].toInt32();
        this.sock_addr = args[4];
        this.to_len = args[5].toInt32();
    },
    onLeave: function (ret) {
        var port = this.sock_addr.add(2).readU16();
        var addr = this.sock_addr.add(4).readU32();
        var data = Memory.readByteArray(this.buffer, ret.toInt32())
        send({
            type: "SEND",
            ptr: this.buffer.toInt32(),
            addr,
            port
        }, data);
        return ret;
    }
})

Interceptor.attach(ptr(recvfrom), {
    onEnter: function (args) {
        this.socket = args[0];
        this.buffer = args[1];
        this.size = args[2].toInt32();
        this.flags = args[3].toInt32();
        this.sock_addr = args[4];
        this.from_len = args[5].toInt32();
    },
    onLeave: function (ret) {
        if (!ret.equals(ptr("0xffffffff"))) {
            var port = this.sock_addr.add(2).readU16();
            var addr = this.sock_addr.add(4).readU32();
            var data = Memory.readByteArray(this.buffer, ret.toInt32())
            send({
                type: "RECV",
                ptr: this.buffer.toInt32(),
                addr,
                port
            }, data);
        }
        return ret;
    }
})