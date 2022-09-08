from typing import List

def f_rec(arr,idx,x):
    if x==0:
        return 0
    if idx==0:
        if x%arr[0]==0: 
            return x//arr[0]
        return float('inf')
    
    wo = f_rec(arr,idx-1,x)
    w = float('inf')

    if arr[idx]<=x:
        combs = x//arr[idx]
        for i in range(1,combs+1): 
            w = min(i + f_rec(arr,idx-1,x-(i*arr[idx])), w)
    return min(w,wo)

def f_mem(arr,idx,x,dp):
    if x==0:
        return 0
    if idx==0:
        if x%arr[0]==0: 
            return x//arr[0]
        return float('inf')
    if dp[idx][x]==-1:
        wo = f_mem(arr,idx-1,x,dp)
        w = float('inf')
        if arr[idx]<=x:
            combs = x//arr[idx]
            for i in range(1,combs+1): 
                w = min(i + f_mem(arr,idx-1,x-(i*arr[idx]),dp), w)
        dp[idx][x] = min(w,wo)
    return dp[idx][x]

def minimumElements(arr: List[int], x: int) -> int:
    # Write your code here.
    n = len(arr)
#     res = f_rec(arr,n-1,x)
    # Memoization
    dp = [ [-1]*(x+1) for _ in range(n)]
    res = f_mem(arr,n-1,x,dp)
    if res==float('inf'):
        res=-1
    return res
