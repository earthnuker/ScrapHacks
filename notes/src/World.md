# World

## Game World/State Pointer @ `0x7fe944`

Points to World struct

 Offset | Type                     | Description                            
 ------ | ------------------------ | -------------------------------------- 
 0x0000 | `void**`                 | Virtual Method Table                   
 0x0004 | `uint32_t`               | Slots in Entity Hashtable              
 0x0008 | `void**`                 | Pointer to Entity Hashtable            
 0x00B0 | `??`                     | Pointer to Ground Object (?)           
 0x0288 | `pyEntity*`              | UsrEntity[0]                           
 0x028C | `pyEntity*`              | UsrEntity[1]                           
 0x0290 | `pyEntity*`              | UsrEntity[2]                           
 0x0294 | `pyEntity*`              | UsrEntity[3]                           
 0x0298 | `uint32_t`               | Slots in Model Hashtable               
 0x029C | `void**`                 | Pointer to Model Hashtable             
 0x02B8 | `uint32_t`               | Slots in Entity lists Hashtable        
 0x02BC | `void**`                 | Pointer to Entity list Hashtable       
 0x0330 | `float[3]`               | Time (why 3 times?)                    
 0x1C6C | `float`                  | Alarm level                            
 0x1C68 | `float`                  | Alarm Grow Level                       
 0x2158 | `float`                  | Used in `World_Init`                   
 0x2170 | `???`                    | Used in `World_Init`                   
 0x2180 | `float`                  | Used in `World_Init`                   
 0x2188 | `void*`                  | Used in `World_Init`                   
 0x218C | `void*`                  | Used in `World_Init`                   
 0x2190 | `float`                  | Used in `World_Init`                   
 0x2198 | `void*`                  | Used in `World_Init`                   
 0x219C | `void*`                  | Used in `World_Init`                   
 0x21A0 | `void**`                 | Used in `World_Init` (VTable pointer?) 
 0x21B4 | `void**`                 | Used in `World_Init` (VTable pointer?) 
 0x21C8 | `???`                    | Used in `World_Init`                   
 0x2204 | `uint32_t` or `uint16_t` | Used in `World_Init`                   
 0x2230 | `float`                  | Used in `World_Init`                   
 0x2238 | `???`                    | Used in `World_Init`                   
 0x2254 | `float`                  | Used in `World_Init`                   
 
## cPyEntity structure

 Offset | Type     | Description          
 ------ | -------- | -------------------- 
 0x0000 | `void**` | Virtual Method Table 
 0x0004 | `char*`  | Name                 
 0x0008 | `void*`  | ???                  


## Entity Hash Table

Hash-function used: [PJW](https://en.wikipedia.org/wiki/PJW_hash_function) (Same parameters as the example implementation)

Entry format:

```cpp
struct HT_Entry {
  void* data;
  const char* key;
  HT_Entry* next;
}
```

Data format:

 Offset | Type          | Description              
 ------ | ------------- | ------------------------ 
 0x0    | `void**`      | Virtual Method Table (?) 
 0x4    | `const char*` | name as string           
 0x14   | `void*`       | pointer to self (why?)   
 0x28   | `float[3]`    | Position in Game World   

## EntityList Hash Table

Attributes:
- `Near`
- `First`
- `Num`
- `OnDeath`
- `OnDamage`
- ...