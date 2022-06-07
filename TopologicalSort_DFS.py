def topologicalSort(adj, v, e):
    # Convert graph to adj matrix
    if v==1 and e==0:
        return [0]
    graph = [[] for i in range(v)]
    for i in range(e):
        graph[adj[i][0]] += [adj[i][1]]  
    sort = []
    visited = []
    #print(graph)
    for start in range(v):
        if start not in visited:
            stack = [start]
            visited += [start]
            
            while(len(stack)>0):
                node = stack[-1]
                count = 0
                for k in graph[node]:
                    if k not in visited:       
                        stack.append(k)
                    else:
                        count+=1
                if count == len(graph[node]):
                    node = stack.pop()
                    if node not in visited:
                        visited.append(node)
                #print(stack)
                #break
                    
    #print(visited)
    visited.reverse()
    return visited

                
    