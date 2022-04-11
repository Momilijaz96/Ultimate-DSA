
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

g = Graph(True);
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,1)


print(g.adjlist)