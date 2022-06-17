from graphs import Graph

def shortest_path(graph,src,visited,dis):
    print(src)
    for k in graph[src]:
        if k not in visited:
            visited.append(k)
            dis[k] = dis[src] + 1
            shortest_path(graph,k,visited,dis)
        dis[k] = min(dis[k], dis[src] + 1)
            

if __name__=='__main__':
    g = Graph(True)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,6)
    g.addEdge(3,4)
    g.addEdge(4,5)
    g.addEdge(5,6)
    g.addEdge(6,7)
    g.addEdge(6,8)
    g.addEdge(7,8)
    print("Graph: ",g.adjlist)
    dis = [0 for i in range(len(g.adjlist))]
    shortest_path(g.adjlist,0,[0],dis)
    print("Distance: ",dis)
