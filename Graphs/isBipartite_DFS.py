class Solution: 
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph)==1 and len(graph[0])==1:
            return False
        stack = []
        color = {}
        for start in range(len(graph)):
            if start not in color:
                stack = [start]
                color[start] = True
                while(len(stack)>0):
                    node = stack.pop()
                    print(node)
                    for kid in graph[node][::-1]:   
                        if kid in color:
                            if color[kid]==color[node]:
                                print("kid color: ",color[kid])
                                print("parent color: ",color[node])
                                return False
                        else:
                            color[kid] = not color[node]
                            stack += [kid] 
        return True

    
    