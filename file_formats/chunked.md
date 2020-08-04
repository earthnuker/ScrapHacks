# General Block format

```cpp
struct Block {
    unsigned char block_id[4],
    uint32_t size,
    unsigned char data[size],
}

template<typename T>
struct Block {
    unsigned char block_id[4],
    uint32_t size,
    T data,
}
```

# Block IDs


| File Extension | Description              |
|----------------|--------------------------|
| .cm3           | Animation file           |
| .sm3           | 3d model file            |
| .dum           | Dummy (map object) file  |
| .pth           | AI Path                  |
| .emi           | Emission maps/Materials? |
| .amc           | ???                      |

| File ID | Chunk IDs                                                                |
|---------|--------------------------------------------------------------------------|
| AMC     | AMC, CMSH, QUAD                                                          |
| CM3     | ANI, CM3, EVA, NAE, NAM, SCN                                             |
| DUM     | DUM, INI                                                                 |
| EMI     | EMI, LFVF, MAP, MAT, TRI                                                 |
| SM3     | ANI, CAM, INI, LFVF, LUZ, MAP, MAT, MD3D, NAE, NAM, PORT, SCN, SM3, SUEL |

| Chunk ID | Description                 |
|----------|-----------------------------|
| ANI      | Animation data?             |
| AMC      | Collision Data              |
| CMSH     | Mesh data?                  |
| INI      | INI-Configuration data      |
| LUZ      | Lighting information        |
| MAT      | Material information        |
| QUAD     | Mesh data?                  |
| SCN      | Scene data?                 |
| CAM      | Camera info?                |
| PORT     | Light portals?              |
| SUEL     | Ground plane?               |
| DUM      | Dummy (map object) data     |
| MAP      | UV Map?                     |
| LFVF     | FVF Vertex Data             |
| TRI      | Triangle strip definitions? |
| NAM,NAE  | Animation Data?             |

# Format of Specific chunks

## INI

Configuration Data

```cpp
struct INI {
    uint32_t num_sections,
    struct {
        uint32_t num_lines,
        struct {
            uint32_t num_chars,
            char line[num_chars]
        } lines[num_lines],
    } sections[num_sections]
}
```


## LFVF

DirectX Flexible Vertex Format Data

```cpp
struct Vertex { // fields according to flags
    float position[3],
    float rhw,
    float weights[3],
    float normal[3],
    float point_size,
    uint32_t diffuse, //RGBA
    uint32_t specular, //RGBA
    float tex_coords[1 to 4][8] // ??? decided by flags?
}

struct LFVF {
    uint32_t unk,
    uint32_t num_entries,
    struct {
        uint32_t FVF, // FVF vertex data configuration
        uint32_t vert_size //?,
        uint32_t num_verts,
        Vertex vertices[num_vers]
    } entry[num_entries]
}
```

## DUM

Map object data

```cpp
struct DUM {
    uint32_t unk_1,
    uint32_t num_dummies,
    uint32_t unk_2,
    struct {
        uint32_t name_length,
        char name[name_length],
        float position[3],
        float rotation[3],
        uint32_t has_ini,
        if (has_ini) {
            Block<INI> ini
        },
        uint32_t unk_1 // has_next?
    } sections[num_sections]
}
```