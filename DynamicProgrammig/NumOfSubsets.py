from typing import List
import numpy as np
def f_recur(arr,idx,tar):
    if idx==0:
        if tar==0 and arr[0]==0: 
            return 2
        if tar==0 or arr[0]==tar:
            return 1
        return 0
    w = 0
    if arr[idx]<=tar:
        w = f_recur(arr,idx-1,tar-arr[idx])
    wo = f_recur(arr,idx-1,tar)
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