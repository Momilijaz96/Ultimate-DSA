import numpy as np
def f_rec(s,idx1,t,idx2,res):
    if idx1==-1 or idx2==-1:
        return res
    if s[idx1]==t[idx2]:
        res =  f_rec(s,idx1-1,t,idx2-1,res+1)
    res = max(res,f_rec(s,idx1-1,t,idx2,0),f_rec(s,idx1,t,idx2-1,0))
    return res

def f_tab(s,t,len_s,len_t):
    dp = np.array([[-1]*(len_t+1) for _ in range(len_s+1)])
    dp[0,:] = 0
    dp[:,0] = 0
    res = 0        
    for idx1 in range(1,len_s+1):
        for idx2 in range(1,len_t+1):
            if s[idx1-1]==t[idx2-1]:
                dp[idx1][idx2] = 1 + dp[idx1-1][idx2-1]
            else:
                dp[idx1][idx2] = 0
            res = max(res,dp[idx1][idx2] )
    return res

def lcs(str1, str2):
    #Write your code here.
    l1 = len(str1)
    l2 = len(str2)
#     res = f_rec(str1,l1,str2,l2,0)
    res = f_tab(str1,str2,l1,l2)
    return res

