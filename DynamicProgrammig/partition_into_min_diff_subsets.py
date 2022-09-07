from sys import stdin, stdout, setrecursionlimit
import numpy as np
setrecursionlimit(10 ** 7)

def f_recur(arr,n,s,idx,cs,d):
    if idx==0:
        dws = abs(s - 2*(cs+arr[0]) )
        return min(d,dws)
    d = min(d, abs(2*cs - s))
    dw = f_recur(arr,n,s,idx-1,cs+arr[idx],d)
    dwo = f_recur(arr,n,s,idx-1,cs,d)
    return min(dw,dwo)

def f_tab(arr,target,n):
    dp = np.array( [[False]*(target+1) for _ in range(n)] )
    dp[0,:] = [arr[0]==i for i in range(target+1)]
    dp[:,0] = True

    for idx in range(1,n):
        for k in range(1,target+1):
            wo = dp[idx-1][k]
            w =  dp[idx-1][k-arr[idx]] if (arr[idx]<=k) else False
            dp[idx][k] = wo or w
    return dp[n-1]
    
def minSubsetSumDifference(arr, n):
    # Write your code here.
    # Return the minimum difference in the form of an integer.
    s = sum(arr)
#     res = f_recur(arr,n,s,n-1,0,float('inf'))

    # Using the target sum problem
    subsets = f_tab(arr,s,n)
    min_diff = float('inf')
    for i in range((s//2)+1):
        if subsets[i]:
            min_diff = min(min_diff, abs((2*i)-s) )
    return min_diff









# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return N, arr


tc = int(input())
while tc > 0:
    N, arr = takeInput()
    ans = minSubsetSumDifference(arr, N)
    stdout.write(str(ans) + "\n")
    tc -= 1
