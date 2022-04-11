#Problem: Find cycle in a given undirected graph, using DFS. Graph has only one component.
from graphs import Graph


def dfs_cycle(graph,visited,elem,p):
    for n in graph.adjlist[elem]:
        if n in visited and n!=p:
            return True
        elif n not in visited:
            visited.append(n)
            res = dfs_cycle(graph,visited,n,elem)
            if res:
                return res
    return False

g = Graph(True);
g.addEdge(3, 5);
g.addEdge(5, 6);
g.addEdge(5, 10);
g.addEdge(6, 7);
g.addEdge(6, 9);
g.addEdge(7, 8);
g.addEdge(10, 9);
g.addEdge(9, 8);
g.addEdge(8, 11);
g.addEdge(10,12)


print(g.adjlist)
visited = []
f = list(g.adjlist.keys())[0]
visited.append(f)
p=f
print(dfs_cycle(g,visited,f,p))

#neighbor that is visited but is not our previous