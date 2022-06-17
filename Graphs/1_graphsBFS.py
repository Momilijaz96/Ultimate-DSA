from graphs import Graph

#Breath First Search - Visiting Adjacent Nodes, graph has just one component

def BFS(graph):
  visited = []
  first = list(graph.adjlist.keys())[0]
  visited.append(first)
  queue = [first]
  while(len(queue)>0) :
    elem = queue.pop(0)
    print(elem)
    for nbr in graph.adjlist[elem]:
      if nbr not in visited:
        visited.append(nbr)
        queue.append(nbr)

g = Graph(True)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,1)

(BFS(g))

#cycle is neighbor that is visited but is not our previous