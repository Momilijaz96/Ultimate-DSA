import numpy as np
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
   
def canPartition(arr, n):
    # Write your code here.
    s = sum(arr)
    if s%2==0:
        return f_sp(arr,s//2,n)
    else:
        return False