def dfs(graph,node,vis,stack):
    for k in graph[node]:
        if k not in vis:
            vis.append(k)
            stack,vis = dfs(graph,k,vis,stack)
    stack.append(node)
    #print(node)
    return stack,vis    

def topo_sort(graph):
    stack = []
    vis = []
    for n in range(len(graph)):
        if n not in vis:
            stack,vis = dfs(graph,n,vis,stack)
    return stack 

def stronglyConnectedComponents(n, edges):
    # Make adjacency list
    graph = [[] for i in range(n)]
    for e in edges:
        graph[e[0]].append(e[1])
    #print(graph)
    
    #Do Topo Sort
    stack = topo_sort(graph)
    #Transpose the graph
    graph = [[] for i in range(n)]
    for e in edges:
        graph[e[1]].append(e[0])
    #DFS in ascending order of finishing time
    vis = []
    scc = []
    while(stack):
        n = stack.pop()
        temp = []
        if n not in vis:
            vis.append(n)
            temp,vis = dfs(graph,n,vis,temp)
            #print(temp)
            scc.append(temp)
    return scc
       