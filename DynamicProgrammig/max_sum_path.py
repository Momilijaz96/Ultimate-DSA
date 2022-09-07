import numpy as np
def f_recur(arr,idx,target):
    if target==0:
        return True
    if idx==0:
        return arr[0]==target
    wo = f_recur(arr,idx-1,target)
    w = False
    if arr[idx]<=target:
        w = f_recur(arr,idx-1,target-arr[idx])
    return w or wo

def f_tab(arr,target,n):
    dp = np.array( [[False]*(target+1) for _ in range(n)] )
    dp[0,:] = [arr[0]==i for i in range(target+1)]
    dp[:,0] = True

    for idx in range(1,n):
        for k in range(1,target+1):
            wo = dp[idx-1][k]
            w =  dp[idx-1][k-arr[idx]] if (arr[idx]<=k) else False
            dp[idx][k] = wo or w
    return dp[n-1][target]
                
def f_sp(arr,target,n):
    prev_row = np.array( [False]*(target+1) )
    prev_row = [arr[0]==i for i in range(target+1)]
    prev_row[0] = True
    row = np.array( [False]*(target+1) )
    row[0] = True
    for idx in range(1,n):
        for k in range(1,target+1):
            wo = prev_row[k]
            w =  prev_row[k-arr[idx]] if (arr[idx]<=k) else False
            row[k] = wo or w
        prev_row = row.copy()
    return prev_row[target]
    

def subsetSumToK(n, target, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
#     res = f_recur(arr,n-1,target)
    res = f_sp(arr,target,n)
    return res
    
    

