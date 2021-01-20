# Packed

```cpp
struct Header {
    unsigned char magic[4]; // always BFPK
    uint32_t version;
    uint32_t number_of_files;
    struct File {
        uint32_t path_length;
        char path[]; // latin1 encoding
        uint32_t data_size;
        uint32_t data_offset; // offset includes header size so it can be used directly in a seek() call
    } files[];
};
```