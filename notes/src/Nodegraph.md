# AI Nodegraph

Used for pathfinding using the A*-Algorithm.

```cpp
// n= number of dimension (3 or 2)

template<size_t n>
struct Node {
    float pos[n];
};

template<size_t n>
struct Edge {
    uint32_t num_edge_nodes;
    Node<n> nodes[];
};

template<size_t n>
struct Graph {
    uint32_t num_nodes;
    Node<n> nodes[];
    uint32_t num_edges;
    Edge<n> edges[];
};
```
