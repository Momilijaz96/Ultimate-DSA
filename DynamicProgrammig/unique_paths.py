from os import *
from sys import *
from collections import *
from math import *

def f(x,y,m,n,ways):
    if (x,y)==(m-1,n-1):
        return 1
    if x>m-1 or y>n-1: return 0
    dwn = f(x+1,y,m,n,ways)
    rit = f(x,y+1,m,n,ways)
    ways += (dwn+rit)
    return ways

def f_mem(x,y,m,n,dp):
    if (x,y)==(m-1,n-1):
        return 1
    if x>m-1 or y>n-1: return 0
    if dp[x][y]==0:
        dwn = f_mem(x+1,y,m,n,dp)
        rit = f_mem(x,y+1,m,n,dp)
        dp[x][y] += (dwn+rit)
    return dp[x][y]

def f_tab(m,n):
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1 #one way to reach start, btm-up
    for i in range(m):
        for j in range(n):
            if i-1>=0:
                dp[i][j] += dp[i-1][j]
            if j-1>=0:
                dp[i][j] += dp[i][j-1]
    return dp[-1][-1]

def f_sp(m,n):
    top = 1
    left = 1
    for i in range(m):
        for j in range(n):
            curr = 0
            if i-1>=0:
                curr += top
                top = curr 
            if j-1>=0:
                curr += left
                left = curr
                top = curr
    return curr

def uniquePaths(m, n):
	# Recursion
# 	return f(0,0,m,n,0)
    
    # Memoization
#     dp = [[0]*n for _ in range(m)]
#     res = f_mem(0,0,m,n,dp)
    
    # Tabulation
#     res = f_tab(m,n)

    #Space Optim
    res = f_sp(m,n)
    return res
