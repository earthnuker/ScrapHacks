# MultiSpriteTable

```cpp
struct Tile {
    uint16_t pos[2];
    uint16_t size[2];
}

struct MST {
    char magic[4]; // always "MST\0"
    uint32_t data_size;
    uint32_t version; // should be 100
    uint32_t image_size[2]; // width and height of base image
    uint32_t num_tiles; // number of tiles/subsprites
    Tile tiles[num_tiles];
}
```