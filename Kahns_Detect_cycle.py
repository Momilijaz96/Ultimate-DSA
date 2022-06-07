def detectCycleInDirectedGraph(n, edges):
    
    graph = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for i in range(len(edges)):
        graph[edges[i][0]-1] += [edges[i][1]-1] 
        indegree[edges[i][1]-1] += 1
 
    q = []
    for node in range(n):
        if indegree[node] == 0:
            q.append(node)
    
    while(len(q)>0):
        node = q.pop()
        for k in graph[node]:
            indegree[k] -= 1
            if indegree[k] == 0:
                q.append(k)
    
    #Check for cycle
    for n in indegree:
        if n>0:
            return 1
    return 0
        