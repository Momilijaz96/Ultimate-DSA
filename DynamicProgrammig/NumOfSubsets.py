from typing import List
import numpy as np
def f_recur(arr,idx,ctar):
    if ctar==0:
        return 1
    if idx==0:
        ans = 1 if (arr[0]==ctar) else 0
        return ans
    w = 0
    if arr[idx]<=ctar:
        w = f_recur(arr,idx-1,ctar-arr[idx])
    wo = f_recur(arr,idx-1,ctar)
    return w+wo

def f_mem(arr,idx,tar,dp):
    if idx==0:
        if tar==0 and arr[0]==0: 
            return 2
        if tar==0 or arr[0]==tar:
            return 1
        return 0
    if dp[idx][tar]==-1:
        w = 0
        if arr[idx]<=tar:
            w = f_mem(arr,idx-1,tar-arr[idx],dp)
        wo = f_mem(arr,idx-1,tar,dp)
        dp[idx][tar] = w+wo
    return dp[idx][tar]



def findWays(arr: List[int], tar: int) -> int:
    # Write your code here.
    #Count zeros
  
    n = len(arr)
#     res = f_recur(arr,n-1,tar)
    dp = [[-1]*(tar+1) for _ in range(n)]
    res = f_mem(arr,n-1,tar,dp)
    
    return res