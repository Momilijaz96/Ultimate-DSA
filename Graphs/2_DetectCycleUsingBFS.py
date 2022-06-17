'''
Problem: Detect cycle in a undirected graph using BFS
Solution: Look for neighbor which has been visited before and is not ur parent, if
        such node exists, it's a cyclic undirected graph else it's not.
'''
from graphs import Graph

def detect_cycle_BFS(graph):
    
    visited=[]
    first_node = list(graph.adjlist.keys())[0]
    visited.append(first_node)
    queue=[]
    queue.append((first_node,first_node))
    
    while(len(queue)>0):
        main = queue.pop(0)
        parent = main[1]
        main = main[0]
        for nbr in graph.adjlist[main]:
            if nbr in visited and nbr!=parent:
                return True
            elif nbr not in visited:
                visited.append(nbr)
                queue.append((nbr,main))
    return False


if __name__=='__main__':
    g = Graph(True)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,5)
    g.addEdge(5,1)
    print(g.adjlist)

    print(detect_cycle_BFS(g))
