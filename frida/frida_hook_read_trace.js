var pak_files = {}
var ftypes = {}
var record=false;

var current_block_id;
var filename;
var t0 = performance.now();

Interceptor.attach(ptr("0x5e3b50"), { //read_block_header
    onEnter: function (args) {
        filename = pak_files[this.context.ecx] || this.context.ecx;
        current_block_id = args[0].readUtf8String();
    },

    onLeave: function(ret) {
        return ret;
    }
})

// Interceptor.attach(ptr("0x5e3c50"), { // read_block_id
//     onEnter: function (args) {
//         var filename=pak_files[this.context.ecx]||this.context.ecx;
//         var id=args[1].readUtf8String();
//         console.log("[+read_block("+filename+")]",id,args[1]);
//     },

//     // onLeave: function(ret) {
//     //     console.log("[-read_ini_block] Ret:",ret);
//     // }
// })

Interceptor.attach(ptr("0x7B43B020"),{
    onEnter: function(args) {
        var info={};
        info['this']=args[0];
        info['Length']=args[1];
        info['Usage']=args[2];
        info['FVF']=args[3];
        info['Pool']=args[4];
        info['ppVertexBuffer']=args[4];
        send({CreateVertexBuffer:info});
    }
})

Interceptor.attach(ptr("0x5e3bb0"), { // read_stream_wrapper
    onEnter: function (args) {
        this.args = {};
        this.args[0] = args[0];
        this.args[1] = args[1];
        this.timestamp = performance.now()-t0;
    },
    onLeave: function (ret) {
        var data=Memory.readByteArray(this.args[0],this.args[1].toInt32());
        var stack = Thread.backtrace(this.context,Backtracer.ACCURATE);
        var obj={
            filename,
            timestamp: this.timestamp,
            block_id: current_block_id,
            stack
        };
        send(obj,data);
    }
})


Interceptor.attach(ptr("0x5e3800"), { // fopen_from_pak
    onEnter: function (args) {
        this.filename = args[0].readUtf8String();
    },
    onLeave: function (ret) {
        if (ret != 0) {
            pak_files[ret] = this.filename;
        }
    }
})

// Interceptor.attach(ptr("0x5e3c50"), { // read_block_id
//     onEnter: function (args) {
//         console.log("[+read]",args[0],args[1]);
//     },
//     onLeave: function(ret) {
//         console.log("[-read] Ret:",ret);
//     }
// })

// Interceptor.attach(ptr("0x6665a0"), { // load_m3d_1
//     onEnter: function (args) {
//         console.log("[M3D_1]",args[0].readUtf8String());
//     }
// })


// Interceptor.attach(ptr("0x666900"), { // load_m3d_2
//     onEnter: function (args) {
//         console.log("[M3D_2]",args[0].readUtf8String());
//     }
// })


function dasm(addr, size) {
    var size = size || 8;
    var offset = 0;
    var ret = [];
    while (ret.length != size) {
        var inst = Instruction.parse(ptr(addr).add(offset));
        ret.push(("[" + inst.address + "] " + inst.mnemonic + " " + inst.opStr).trim());
        offset += inst.size;
    }
    return ret;
}

function r(addr, options) {
    var options = options || {}
    var max_depth = options.max_depth || 4;
    var num = options.num || 4;
    var ret = {};
    var vals = [
        "S8",
        "U8",
        "S16",
        "U16",
        "S32",
        "U32",
        "Float",
        "Double",
        "Pointer",
        "CString",
        "Utf8String",
        "Utf16String",
        "AnsiString"
    ];
    vals.forEach(function (k) {
        try {
            ret[k] = ptr(addr)['read' + k]()
        } catch (e) {
            ret[k] = undefined;
        }
    })
    try {
        ret["code"] = dasm(addr, 8);
    } catch (e) {
        ret["code"] = undefined;
    }

    if (max_depth > 1) {
        var p = {};
        var read_ptr = false;
        for (var i = 0; i < num; ++i) {
            if (ret["Pointer"] === undefined) {
                continue;
            }
            p[i * Process.pointerSize] = r(ret["Pointer"].add(i * Process.pointerSize), {
                max_depth: max_depth - 1,
                num
            });
            read_ptr = true;
        }
        if (read_ptr) {
            ret["p"] = p;
        }
    }
    return ret;
}


// function test() {
//     for (var p = 0; p < 4; ++p) {
//         var player = ptr(0x7FE944).readPointer().add(0x288 + p * 4).readPointer();
//         if (!player.isNull()) {
//             console.log("Player " + (p+1) + ":", player);
//             console.log(JSON.stringify(r(player),null,4));
//         }
//     }
// }
