var stalked_threads = [];
var excluded_modules = []
var sent=false;
setInterval(() => {
    Process.enumerateModules().forEach(mod => {
        if (mod.name == "Scrap.exe") {
            if (!sent) {
                send({
                    mod: mod
                })
                sent=true;
            }
            return;
        }
        if (excluded_modules.indexOf(mod.name) == -1) {
            Stalker.exclude(mod);
            excluded_modules.push(mod.name);
        }
    })
    Process.enumerateThreads().forEach(thread => {
        if (stalked_threads.indexOf(thread.id) != -1) {
            return;
        }
        Stalker.follow(thread.id, {
            events: {
                call: true,
                block: true,
                compile: true,
                ret: true,
                exec: true
            },
            onReceive: function (events) {
                send({
                    stalker: Stalker.parse(events, {
                        annotate: true,
                        stringify: true
                    })
                });
            }
        })
        stalked_threads.push(thread.id);
    })
}, 0)