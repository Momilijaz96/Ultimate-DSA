from graphs import Graph

def DFS(graph,visited,elem):
    print(elem)
    for n in graph.adjlist[elem]:
        if n not in visited:
            visited.append(n)
            DFS(graph,visited,n)

if __name__=='__main__':
    g = Graph(True)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,5)
    g.addEdge(5,1)
    print(g.adjlist)

    visited=[1]
    elem=1
    (DFS(g,visited,elem))

