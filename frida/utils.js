
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
