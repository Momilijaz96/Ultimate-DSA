
class Graph:
  def __init__(self, undirected):
    self.adjlist = {  };
    self.undir = undirected;
    self.weights = { }

  def addEdge(self, u, v, w=1):
    if u not in self.adjlist:
      self.adjlist[u] = [];
      self.weights[u] = []
    if v not in self.adjlist:
      self.adjlist[v] = [];
      self.weights[v] = []

    self.adjlist[u].append(v);
    self.weights[u].append(w);
    if self.undir:
      self.adjlist[v].append(u);
      self.weights[v].append(w);

  def getAdjList(self):
    return self.adjlist;
  
  def getweight(self, src , child_idx):
    return self.getweight[src][child_idx] #child_idx in parent adj list

g = Graph(True);
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,1)


