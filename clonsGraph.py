# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def cloneGraph(node):
    # Write your code here.
    deepcopy = graphNode(node.data,node.neighbours)
    vis = [node.data]
    q = [deepcopy]
    new_nodes ={node.data : deepcopy}
    while(len(q)>0):
        print("visited: ",vis)
        node = q.pop(0)
        print(node.data)
        print(node.neighbours)
            
        for idx,k in enumerate(node.neighbours):
            if k.data not in vis:
                print("child: ",k.data)
                print("child nbrs: ",k.neighbours)
                vis.append(k.data)
                new_kid = graphNode(k.data,k.neighbours)
                q.append(new_kid) 
                new_nodes[k.data] = new_kid
            node.neighbours[idx] = new_nodes[k.data]
        print(node.neighbours)
    return deepcopy            
    
    
