#Problem Link: https://leetcode.com/problems/is-graph-bipartite/submissions/

class Solution:
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        if len(graph)==1 and len(graph[0])==1:
            return False
        
        q = []
        color = {}
        
        for start in range(len(graph)):
            if start not in color:
                q.append(start)
                color[start] = True

                while(len(q)>0):        

                    node = q.pop(0)
                    for kid in graph[node]:   
                        if kid in list(color.keys()):
                            if color[kid]==color[node]:
                                return False
                        elif kid not in list(color.keys()):
                            color[kid] = not color[node]
                            q.append(kid)

        return True
