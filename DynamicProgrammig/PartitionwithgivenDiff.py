from typing import List
import numpy as np

def f_recur(arr,idx,ctar):
    if idx==0:
        if ctar==0 and arr[0]==0:
            return 2
        if ctar==0 or arr[0]==ctar:
            return 1
        return 0
    w = 0
    if arr[idx]<=ctar:
        w = f_recur(arr,idx-1,ctar-arr[idx])
    wo = f_recur(arr,idx-1,ctar)
    return w+wo

def f_mem(arr,idx,ctar,dp):
    if idx==0:
        if ctar==0 and arr[0]==0:
            return 2
        if ctar==0 or arr[0]==ctar:
            return 1
        return 0
    if dp[idx][ctar]==-1:
        w = 0
        if arr[idx]<=ctar:
            w = f_mem(arr,idx-1,ctar-arr[idx],dp)
        wo = f_mem(arr,idx-1,ctar,dp)
        dp[idx][ctar] = w+wo
    return dp[idx][ctar]

def f_tab(arr,n,tar):
    dp = np.array( [ [-1]*(tar+1) for _ in range(n)] )
    dp[0,:] = 0
    if arr[0]==0:
        dp[0,0] = 2
    else:
        dp[0,0] = 1
    if arr[0]<=tar and arr[0]!=0:
        dp[0,arr[0]] = 1
    for idx in range(1,n):
        for ctar in range(tar+1):
            w = 0
            if arr[idx]<=ctar:
                w = dp[idx-1][ctar-arr[idx]]
            wo = dp[idx-1][ctar]
            dp[idx][ctar] = w+wo
    return dp[n-1][tar]


def f_sp(arr,n,tar):
    prev_row =  [0]*(tar+1)
    if arr[0]==0:
        prev_row[0] = 2
    else:
        prev_row[0] = 1
    if arr[0]<=tar and arr[0]!=0:
        prev_row[arr[0]] = 1
    for idx in range(1,n):
        row =  [0]*(tar+1)
        for ctar in range(tar+1):
            w = 0
            if arr[idx]<=ctar:
                w = prev_row[ctar-arr[idx]]
            wo = prev_row[ctar]
            row[ctar] = w+wo
        prev_row = row
    return prev_row[tar]

def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    s = sum(arr)
    if (d+s)%2>0:
        return 0
    tar = (d+s)//2
#     res = f_recur(arr,n-1,tar)
#     dp = [ [-1]*(tar+1) for _ in range(n)]
#     res = f_mem(arr,n-1,tar,dp)
    res = f_sp(arr,n,tar)
    return res % ((10**9)+7)