from construct import *

AI_PATH = "Path" / Struct(
    "num_nodes" / Int32ul,
    "nodes" / Float32l[3][this.num_nodes],
    "edges" / PrefixedArray(Int32ul, Float32l[3])[this.num_nodes],
)

data = AI_PATH.parse_file(sys.argv[1])

nodes = [tuple(node) for node in data.nodes]
edges = [[nodes.index(tuple(p)) for p in edge] for edge in data.edges]

# Run in Blender:
"""
import bpy
import numpy as np
import itertools as ITT

nodes = <paste_nodes>
edges_=<paste_edges>

# pasted node and edges here

edges=[]

for edge in edges_:
    for a,b in zip(edge,edge[1:]):
        edges.append(a)
        edges.append(b)

nodes=[[p*0.0001 for p in node] for node in nodes]

me = bpy.data.meshes.new("Test")

nodes = np.array(list(ITT.chain.from_iterable(nodes)))

me.vertices.add(len(nodes)//3)
me.vertices.foreach_set("co", nodes)
me.edges.add(len(edges)//2)
me.edges.foreach_set("vertices", np.array(edges))

me.update(calc_edges=True)
me.validate()

ob = bpy.data.objects.new("Test", me)

scene = bpy.context.scene
scene.collection.objects.link(ob)
"""