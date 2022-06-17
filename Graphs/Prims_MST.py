import numpy as np
def kruskalMST(n, m, graph):
   
    # Write your code here.
    g = [[] for i in range(n)]
    w = [[] for i in range(n)]
    for edge in graph:
        g[edge[0]-1].append(edge[1]-1)
        g[edge[1]-1].append(edge[0]-1)
        w[edge[0]-1].append(edge[2])
        w[edge[1]-1].append(edge[2])

    mst = [1000000 for i in range(n)]
    mst = 0
    visited = [0]
    
    while(len(visited)<n):
        min_wt_dst_node = -1
        min_wt = 10000000
        for node in visited:
            for idx,k in enumerate(g[node]):
                if min_wt > w[node][idx] and k not in visited:
                    min_wt = w[node][idx]
                    min_wt_dst_node = k

        if min_wt_dst_node!=-1:
            visited.append(min_wt_dst_node)
            mst += min_wt
        #print("Min node: ",min_wt_dst_node)
        #print("Min wt: ",min_wt)
        #print("Visited: ",visited)            
           
    #print(visited)
    return mst
                