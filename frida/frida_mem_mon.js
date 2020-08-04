MemoryAccessMonitor.enable({
    base: ptr("0x7fe944"),
    size: 4
}, {
    onAccess: function (details) {
        console.log(details.operation, details.from, details.address)
    },
})