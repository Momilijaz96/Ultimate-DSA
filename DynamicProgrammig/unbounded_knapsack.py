import numpy as np

def f_rec(idx,cap,profit,weight):
    if cap==0:
        return 0
    if idx==0:
        if cap>=weight[0]: 
            return profit[0] * (cap//weight[0])
        return 0
    wo = f_rec(idx-1,cap,profit,weight)
    w = 0
    if weight[idx]<=cap:
        w = profit[idx] + f_rec(idx,cap-weight[idx],profit,weight)
    return max(w,wo)

def f_mem(idx,cap,profit,weight,dp):
    if cap==0:
        return 0
    if idx==0:
        if cap>=weight[0]: 
            return profit[0] * (cap//weight[0])
        return 0
    if dp[idx][cap]==-1:
        wo = f_mem(idx-1,cap,profit,weight,dp)
        w = 0
        if weight[idx]<=cap:
            w = profit[idx] + f_mem(idx,cap-weight[idx],profit,weight,dp)
        dp[idx][cap] = max(w,wo)
    return dp[idx][cap]

def f_tab(n,capacity,profit,weight):
    dp = np.array([[-1]*(capacity+1) for i in range(n)])
    dp[:,0] = 0
    for i in range(capacity+1):
        if i>=weight[0]: 
           dp[0,i] = profit[0] * (i//weight[0])
        else:
           dp[0,i] = 0
    for idx in range(1,n):
        for cap in range(capacity+1):   
            wo = dp[idx-1,cap] 
            w = 0
            if weight[idx]<=cap:
                w = profit[idx] + dp[idx][cap-weight[idx]] 
            dp[idx][cap] = max(w,wo)
    return dp[n-1][capacity]

def f_sp(n,capacity,profit,weight):
    prev = [-1]*(capacity+1)
    prev[0] = 0
    for i in range(capacity+1):
        if i>=weight[0]: 
           prev[i] = profit[0] * (i//weight[0])
        else:
           prev[i] = 0
        
    for idx in range(1,n):
        curr = [-1]*(capacity+1)
        for cap in range(capacity+1):   
            wo = prev[cap] 
            w = 0
            if weight[idx]<=cap:
                w = profit[idx] + curr[cap-weight[idx]] 
            curr[cap] = max(w,wo)
        prev = curr
    return prev[-1]

def unboundedKnapsack(n, w, profit, weight):
    # Write Your code here.
#     res = f_rec(n-1,w,profit,weight)
#     dp = [[-1]*(w+1) for i in range(n)]
#     res = f_mem(n-1,w,profit,weight,dp)
    res = f_sp(n,w,profit,weight)
    return res