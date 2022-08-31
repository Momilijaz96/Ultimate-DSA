def frogJumpK(h,i,k,dp):
    if i==0:
        return 0
    if i>len(dp): #[i]==-1:
        mm_steps = float('inf')
        for j in range(1,k+1):
            if i>=j:
                if dp[i-j]!=-1:
                    dp[i-j] = frogJumpK(h,i-j,k,dp)
                mm_steps = min(mm_steps, dp[i-j] + abs(h[i]-h[i-j]))
        dp[i] = mm_steps
    return dp[i]

h = [40,10,20,70,80,10,20,70,80,60]
dp = []
res = frogJumpK(h,len(h)-1,4,dp) 
print(res)

