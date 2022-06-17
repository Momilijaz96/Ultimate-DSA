def bellmonFord(n, m, src, dest, edges):
    # Write your code here.
    dis = [10000000] * n
    dis[src-1] = 0
    count = 0
    while(count < n-1):
        for u,v,w in edges:
            if dis[u]+w < dis[v]:
                dis[v] = dis[u] + w
        count+=1
    return dis[dest]
