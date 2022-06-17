# Problem: Find cycle in a given undirected graph, using DFS. Graph has only one component.
# Solution: Look for a node that is not ur parent and has been visited before.

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

g = Graph(True)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
#g.addEdge(5,1)
g.addEdge(6,7)
g.addEdge(8,7)


print(g.adjlist)
visited = []
f = list(g.adjlist.keys())[0]
visited.append(f)
p=f
print(dfs_cycle(g,visited,f,p))
