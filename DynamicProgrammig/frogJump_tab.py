from typing import *



def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1]*(n)
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2,n):
        e1,e2 = dp[i-1],dp[i-2]
        c1 = abs(heights[i]-heights[i-1]) + e1 
        c2 = abs(heights[i]-heights[i-2]) + e2
        dp[i] = min(c1,c2)
        
    return dp[-1]
