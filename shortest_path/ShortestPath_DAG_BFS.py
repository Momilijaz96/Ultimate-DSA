from graphs import Graph

def shortest_path(graph,w,src,n):
    q = [src]
    visited = [src]
    path = [0 for i in range(n)]
    while(len(q) > 0):
        node  = q.pop(0)
        for idx,k in enumerate(graph[node]):
            if k not in visited and path[k]==0:
                path[k] = path[k] + path[node] + w[node][idx]
                q.append(k)
                visited.append(k)
            else:
                new_path = path[node] + w[node][idx]
                path[k] = min(path[k],new_path)
                
    return path            

if __name__=='__main__':
    g = Graph(False)
    g.addEdge(0,1,2)
    g.addEdge(1,2,3)
    g.addEdge(2,3,6)
    g.addEdge(0,4,1)
    g.addEdge(4,2,2)
    g.addEdge(4,5,4)
    g.addEdge(5,3,1)

    print("Graph: ",g.adjlist)
    print("Weights: ",g.weights)
    dis = shortest_path(g.adjlist,g.weights,0,len(g.adjlist))
    print("Distance: ",dis)
