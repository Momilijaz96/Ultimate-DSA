#Problem Link: https://leetcode.com/problems/critical-connections-in-a-network/submissions/
class Solution:
    def dfs(self,graph,node,low,it,parent,time,bridge):
        low[node] = time
        it[node] = time
        for k in graph[node]:
            if it[k]==0:
                bridge = self.dfs(graph,k,low,it,node,time+1,bridge)
                low[node] = min(low[k],low[node])
                
                if low[k]>it[node]:
                    bridge.append([node,k])
            elif k!=parent: #cycle detected: visiting a visited node, i.e not parent
                low[node] = min(low[k],low[node])
         
        return bridge 
                
        
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        for e in connections:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        print(graph)
        low = [0] * n
        it = [0] * n
        bridge = []
        bridge = self.dfs(graph,0,low,it,0,0,bridge)
        return bridge