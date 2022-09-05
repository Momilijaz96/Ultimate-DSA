from os import *
from sys import *
from collections import *
from math import *

def f_recur(x,y):
    if x==0 and y==0:
        return 1
    if x<0 or y<0:
        return 0
    top = f_recur(x-1,y)
    left = f_recur(x,y-1)
    return top+left

def f_mem(x,y,dp):
    if x==0 and y==0:
        return 1
    if x<0 or y<0:
        return 0
    if dp[x][y]==-1:
        top = f_mem(x-1,y,dp)
        left = f_mem(x,y-1,dp)
        dp[x][y] = top+left
    return dp[x][y]

def f_tab(m,n):
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if i+1<m:
                dp[i+1][j] += dp[i][j]
            if j+1<n:
                dp[i][j+1] += dp[i][j]
    return dp[-1][-1]

def f_sp(m,n):
    row = [1]*n
    for i in range(m-1):
        next_row = [0]*n
        for j in range(n):
            if i+1<m:
                next_row[j] += row[j]
            if j+1<n:
                row[j+1] += row[j]
        row = next_row.copy()
    return row[-1]

def uniquePaths(m, n):
    # Recursive solution
    #res = f_recur(m-1,n-1)

    # Memoization
#     dp = [[-1]*n for _ in range(m)]
#     res = f_mem(m-1,n-1,dp)

    # Tabulation
#     res = f_tab(m,n)

    #Space Optimization
    res = f_sp(m,n)
    return res