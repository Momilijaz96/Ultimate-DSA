def detectCycleInDirectedGraph(n, edges):
    # Write your code here
    graph = [[] for i in range(v)]
    for i in range(e):
        graph[adj[i][0]] += [adj[i][1]]  
    q = []
    visited = []
    for start in range(n):
        if start not in visited:
            q.append((start,start))
            visited.append(start)
            
            while(len(q)>0):
                node_par = q.pop()
                node = node_par[0]
                parent = node_par[1]
                
                for k in graph[node]:
                    if k in visited and k!=parent:
                        return True
                    elif k not in visited:
                        q.append((node,k))
    return True  
                        
                        
                        
    