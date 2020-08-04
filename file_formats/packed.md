# Format
```cpp
struct Packed {
    unsigned char magic[4], // always BFPK
    uint32_t version,
    uint32_t number_of_files,
    struct File {
        uint32_t path_length,
        char path[path_length], // latin1 encoding
        uint32_t data_size,
        uint32_t data_offset
    } files[number_of_files],
    char data[]
}
```