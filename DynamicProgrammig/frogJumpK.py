def frogJumpK(h,idx,k):
    dp = [0]
    dp.append(abs(h[1]-h[0]))
    for i in range(1,idx):
        mm_steps = float('inf')
        for j in range(1,k+1):
            print(dp,i,j)
            if i-j>=0: # and i-j<len(dp):
                jmp = dp[i-j]
                mm_steps = min(mm_steps, jmp + abs(h[i]-h[i-j]))
        dp.append(mm_steps)
        if len(dp)>k+1:
            dp = dp[-k+1:]
    return dp[-1]

h = [40,10,20,70,80,10,20,70,80,60]
k = 4
#dp = [-1]*len(h)
res = frogJumpK(h,len(h),k) 
print(res)

