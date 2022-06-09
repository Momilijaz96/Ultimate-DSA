from graphs import Graph

def shortest_path(graph,src,n):
    q = [src]
    visited = [src]
    path = [0 for i in range(n)]
    while(len(q) > 0):
        node  = q.pop(0)
        for k in graph[node]:
            if k not in visited and path[k]==0:
                path[k] = path[k] + path[node] + 1
                q.append(k)
                visited.append(k)
            else:
                new_path = path[node] + 1
                path[k] = min(path[k],new_path)
                
    return path          


if __name__=='__main__':
    g = Graph(True)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,3)
    g.addEdge(1,2)
    g.addEdge(4,1)
    g.addEdge(4,3)
    print("Graph: ",g.adjlist)

    print(shortest_path(g.adjlist,0,len(g.adjlist)))