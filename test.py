def graphColoring(mat,m):
    if len(mat)==1 or len(mat[0])==1:
        return "YES"
    if m==1 and len(mat)==1 or len(mat[0])==1 :
        return "YES"
    elif m==1 and len(mat)>1:
        return "NO"
    #Convert graph to the desired notation
    for i,node in enumerate(mat):
        mat[i] = [i for i, e in enumerate(node) if e != 0]
    
    q = [0]
    visited = {0:0}
    for comp in range(len(mat)):
        if comp not in visited:
            q = [comp]
            visited = {comp[0]:0}
        while(len(q)>0):
            node = q.pop(0)
            pcolor = visited[node]
            for k in mat[node]:
                kcolor = (visited[node] + 1) % m 
                if k not in visited:
                        visited[k] = kcolor
                        q.append(k)
                elif visited[k] == pcolor:  #If a visited node has parents' color, its not mp
                        return "NO"

    return "YES"
