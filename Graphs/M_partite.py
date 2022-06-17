def getColor(graph,node,vis,m):
    colors = [0] * m
    for k in graph[node]:
        colors[vis[k]] = 1
    for idx,c in enumerate(colors):
        if c==0:
            return colors[idx]
    return -1
        
def dfs(graph,node,color,m,vis):
    
    if color==-1: return False
    vis[node] = color
    res = True
    for idx,k in enumerate(graph[node]):
        print(node,idx)
        print(vis)
        if k==1 and vis[idx]==-1:
            color = getColor(graph,k,vis,m)
            res = dfs(graph,idx,color,m,vis)
            if not res:
                return res
        elif k==1 and vis[idx]==vis[node]:
            return False
    return res

def graphColoring(mat,m):
    #print(mat)
    #print(sum([sum(m) for m in mat]))
    if m==1 and len(mat)==1:
        return "YES"
    elif sum([sum(m) for m in mat])==0:
        return "YES" 
    elif m==1 and len(mat)>0:
        return "NO"
    elif m==0:
        return "NO"
    
    #Convert adj matrix to adj list
    vis = [-1] * len(mat)
    res = dfs(mat,0,0,m,vis)
    if res:
        return "YES"
    else:
        return "NO"
    
