def topologicalSort(adj, v, e):
    if v==1 and e==0:
        return [0]
    graph = [[] for i in range(v)]
    for i in range(e):
        graph[adj[i][0]] += [adj[i][1]] 
    
    q = []
    indegree = [0 for i in range(v)]

    #Populate indegree
    for i in range(e):
        indegree[adj[i][1]] += 1 
        
    for n in range(v):
       if indegree[n]==0:
           q.append(n)
    res = []
    while(len(q)>0):
        node  = q.pop(0)
        res.append(node)
        for k in graph[node]:
            indegree[k] -= 1
            if indegree[k] == 0:
                q.append(k)
               
    return res   