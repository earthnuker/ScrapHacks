# Chunked Formats

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

 File ID | Chunk IDs                                                                      
 ------- | ------------------------------------------------------------------------------ 
 AMC     | AMC, CMSH, QUAD                                                                
 CM3     | ANI, CM3, EVA, NAE, NAM, SCN                                                   
 DUM     | DUM, INI                                                                       
 EMI     | EMI, LFVF, MAP, MAT, TRI                                                       
 SM3     | ANI, CAM, INI, LFVF, LUZ, MAP, MAT, MD3D, NAE, NAM, PORT, SCN, SM3, SPR3, SUEL 

Read types:

- `i`: 4-byte unsigned integer
- `s`: 4-byte signed integer
- `p`: length prefixed string
- `f`: 4-byte float
- `3f`: array of 3 4-byte floats
- `3i`: array of 3 4-byte unsigned integers

 Chunk ID | Description                 | Reads                    
 -------- | --------------------------- | ------------------------ 
 AMC      | Collision Data              |                          
 ANI      | Animation data?             |                          
 CAM      | Camera info?                |                          
 CMSH     | Collision Mesh Data         |                          
 DUM      | Dummy (map object) data     |                          
 INI      | INI-Configuration data      |                          
 LFVF     | FVF Vertex Data             |                          
 LUZ      | Lighting information        |                          
 MAP      | UV Map?                     |                          
 MAT      | Material information        |                          
 NAE      | Animation Data?             |                          
 NAM      | Animation Data?             |                          
 PORT     | Map portals?                | i==1, i, i, 4, 4         
 QUAD     | Mesh data?                  |                          
 SCN      | Scene data?                 |                          
 SUEL     | Ground plane?               | 0x18, 0xc, 4, 4, 4, 0x18 
 TRI      | Triangle strip definitions? |                          
 MD3D     | 3D Model definition?        |                          

# Format of Specific chunks

## INI

Configuration Data

```cpp
struct INI {
    uint32_t num_sections;
    struct {
        uint32_t num_lines;
        struct {
            uint32_t num_chars;
            char line[num_chars]
        } lines[num_lines];
    } sections[num_sections];
};
```


## LFVF

DirectX Flexible Vertex Format Data

```cpp
struct Vertex { // fields according to flags
    float position[3]; // D3DFVF_XYZ | D3DFVF_XYZRHW | D3DFVF_XYZB*
    float rhw; // D3DFVF_XYZRHW
    float weights[3]; // D3DFVF_XYZB*
    float normal[3]; // D3DFVF_NORMAL
    float point_size; // D3DFVF_PSIZE
    uint32_t diffuse; // D3DFVF_DIFFUSE, RGBA
    uint32_t specular; //D3DFVF_SPECULAR, RGBA
    float tex_coords[D3DFVF_TEXTUREFORMAT][D3DFVF_TEX]; // D3DFVF_TEX* and D3DFVF_TEXTUREFORMAT*
};

struct LFVF {
    uint32_t unk;
    uint32_t num_entries;
    struct {
        uint32_t FVF; // FVF vertex data configuration
        uint32_t vert_size; //?,
        uint32_t num_verts;
        Vertex vertices[num_vers];
    } entry[num_entries];
};
```

## DUM

Map object data

```cpp
struct DUM {
    uint32_t unk_1;
    uint32_t num_dummies;
    uint32_t unk_2;
    struct {
        uint32_t name_length;
        char name[name_length];
        float position[3];
        float rotation[3];
        uint32_t has_ini;
        if (has_ini) {
            Block<INI> ini;
        };
        uint32_t unk_1; // has_next?
    } sections[num_sections];
};
```

## MAP

```cpp
struct MAP {
    uint32_t version;
    uint32_t tex_name_len;
    char tex_name[tex_name_len];
    // TODO: rest
}
```