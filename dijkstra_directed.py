import numpy as np

def dijkstra(vec, vertices, edges, src):
   
    # Write your code here.
    graph = [[] for i in range(vertices)]
    weights = [[] for i in range(vertices)]
    #print("source: ",src)
    
    for e in vec:
        #if e[1] not in graph[e[0]] and e[0] not in graph[e[1]]:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        weights[e[0]].append(e[2])
        weights[e[1]].append(e[2])
        #if e[1]==10:
            #print(e)
       
    #print(len(vec))
    #print(len(weights))
    #print(vec)
    
    q = [src] 
    dq = [0] 
    dis = [2147483647] * vertices
    dis[src] = 0
    
    while(len(q) > 0):
        node = q.pop(0)
        dq.pop(0)
        dist_node = dis[node]
        #print("Source: ",node)

        for idx,k in enumerate(graph[node]):
            if dis[k] > weights[node][idx] + dist_node:
                dis[k] =  weights[node][idx] + dist_node
                q.append(k)
                dq.append(dis[k])
        
        print("dq: ",dq)
        print("q: ",q)
        #myorder = np.argsort(np.array(dq))
        #q = [q[i] for i in myorder]
        #dq = [dq[i] for i in myorder]
        #print("q: ",q)
        #print("dq: ",dq)
   
    return dis
    
    