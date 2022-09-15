
from sys import stdin
import numpy as np

def f_rec(s,idx1,t,idx2):
    if idx1<0 or idx2<0:
        return 0
    if s[idx1]==t[idx2]:
        return 1 + f_rec(s,idx1-1,t,idx2-1)
    else:
        return max(f_rec(s,idx1-1,t,idx2),f_rec(s,idx1,t,idx2-1))

def f_mem(s,idx1,t,idx2,dp):
    if idx1==0 or idx2==0:
        return 0
    
    if dp[idx1][idx2]==-1:
        if s[idx1-1]==t[idx2-1]:
            dp[idx1][idx2] = 1 + f_mem(s,idx1-1,t,idx2-1,dp)
        else:
            dp[idx1][idx2] = max(f_mem(s,idx1-1,t,idx2,dp),f_mem(s,idx1,t,idx2-1,dp))
    return dp[idx1][idx2]

def f_tab(s,t,len_s,len_t):
    dp = np.array([[-1]*(len_t+1) for _ in range(len_s+1)])
    dp[0,:] = 0
    dp[:,0] = 0
    for idx1 in range(1,len_s+1):
        for idx2 in range(1,len_t+1):
            if s[idx1-1]==t[idx2-1]:
                dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
            else:
                dp[idx1][idx2] = max(dp[idx1-1][idx2],dp[idx1][idx2-1])
    return dp[len_s][len_t],dp
        
def lcs(s, t) :
#     res = f_rec(s,len(s)-1,t,len(t)-1)
    len_s = len(s)
    len_t = len(t)
#     dp = [[-1]*(len_t+1) for _ in range(len_s+1)]
#     res = f_mem(s,len_s,t,len_t,dp)
    res,dp = f_tab(s,t,len_s,len_t)
    
    # Print LCS
#     i = dp.shape[0]-1
#     j = dp.shape[1]-1
#     lcs_str = ''
#     while(i>0 and j>0):
#         if s[i-1]==t[j-1]:
#             lcs_str += s[i-1]
#             i-=1
#             j-=1
#         else:
#             if dp[i-1][j]>dp[i][j-1]:
#                 i,j = i-1,j
#             else:
#                 i,j = i,j-1
#     print(lcs_str)
    return res






























    


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))