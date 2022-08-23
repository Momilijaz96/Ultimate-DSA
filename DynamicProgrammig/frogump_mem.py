from typing import *

def func(heights,idx,energy,dp):
    if idx<=0:
        return 0
    elif idx==1:
        return abs(heights[idx]-heights[idx-1])
    
    if dp[idx]==-1:
        e1,e2 = ( func(heights,idx-1,energy,dp), func(heights,idx-2,energy,dp) )
        c1 = abs(heights[idx]-heights[idx-1]) + e1
        c2 = abs(heights[idx]-heights[idx-2]) + e2
        energy += min(c1,c2)
        dp[idx] = energy
    
    return dp[idx]

def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1]*(n)
    return func(heights,n-1,0,dp)
    # Write your code here.
    
