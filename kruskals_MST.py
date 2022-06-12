import numpy as np

class Node:
    def __init__(self,v=-1):
        self.parent = self
        self.value = v

class disjointSet:
    def __init__(self,n):
        self.num_comp = n
        self.rank = [0]*n
    
    def Union(self,a,b):
        pa = a.parent
        pb = b.parent
        ra = self.rank[a.value]
        rb = self.rank[b.value]
        if ra>rb:
            pb.parent = pa
        elif rb>ra:
            pa.parent = pb
        else:
            pa.parent = pb
            self.rank[pb.value] += 1
    
    def FindParent(self,c):
        inp = c
        if c.parent==c: return c
        while(c.parent != c):
            c = c.parent
        final_parent = c
        c = inp
        while(c.parent!=c):
            old_p = c.parent
            c.parent = final_parent
            c = old_p
        return final_parent

def kruskalMST(n, m, graph):
   
    # Write your code here.
    edges = []
    wts = []
    for edge in graph:
        edges.append( (edge[0]-1,edge[1]-1) )
        wts.append(edge[2])
    
    # Create components out of every node
    node_graph = [Node(i) for i in range(n)]
    dg = disjointSet(n)













































































    \
    # Sort edges in asc order of weights
    myorder = np.argsort(wts)
    edges = [edges[i] for i in myorder]
    wts = [wts[i] for i in myorder]
    
    # Create MST
    mst = 0
    for e,w in zip(edges,wts):
        
        pa = dg.FindParent(node_graph[e[0]])
        pb = dg.FindParent(node_graph[e[1]])
        if pa!=pb:   
            dg.Union(node_graph[e[0]], node_graph[e[1]])
            mst += w
    
    return mst
    
    
    
    