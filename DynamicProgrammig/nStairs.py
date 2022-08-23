def func(n,dp):
    if n==1 or n==0:
        return 1
    if dp[n]==-5:
        dp[n]=func(n-1,dp)+func(n-2,dp)
    return dp[n]

def countDistinctWays(n: int) -> int:
    #  Write your code here.
    mod = 1000000007
    if n<=1:
        return 1
    s0 = 1
    s1 = 1
    c = 0
    for i in range(2,n+1):
         olds0 = s0
         s0 = s1
         s1 = (s1+olds0) % mod
    return s1
    
