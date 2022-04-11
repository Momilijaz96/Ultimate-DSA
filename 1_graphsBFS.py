class Graph:
  def __init__(self, undirected):
    self.adjlist = {  };
    self.undir = undirected;

  def addEdge(self, u, v):
    if u not in self.adjlist:
      self.adjlist[u] = [];
    if v not in self.adjlist:
      self.adjlist[v] = [];

    self.adjlist[u].append(v);
    if self.undir:
      self.adjlist[v].append(u);

  def getAdjList(self):
    return self.adjlist;

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

print(g.adjlist)
(BFS(g))

#neighbor that is visited but is not our previous