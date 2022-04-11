import numpy as np
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