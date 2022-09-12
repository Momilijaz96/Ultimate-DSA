from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
import numpy as np

def f_rec(denm,idx,tar):
    if tar==0:
        return 1
    if idx==0:
        if tar%denm[idx]==0:
            return 1
        return 0
    wo =  f_rec(denm,idx-1,tar)
    w = 0
    if denm[idx]<=tar:
        w =  f_rec(denm,idx,tar-denm[idx])
    return w+wo

def f_mem(denm,idx,tar,dp):
    if tar==0:
        return 1
    if idx==0:
        if tar%denm[idx]==0:
            return 1
        return 0
    if dp[idx][tar]==-1:
        wo =  f_mem(denm,idx-1,tar,dp)
        w = 0
        if denm[idx]<=tar:
            w =  f_mem(denm,idx,tar-denm[idx],dp)
        dp[idx][tar] = w+wo
    return dp[idx][tar]

def f_tab(denm,target,n):
    dp = np.array([[-1]*(target+1) for _ in range(n)])
    dp[:,0] = 1
    for t in range(target+1):
        if t%denm[0]==0:
            dp[0,t] = 1
        else:
            dp[0,1] = 0
    for idx in range(1,n):
        for tar in range(target+1):
            wo =  dp[idx-1][tar]
            w = 0
            if denm[idx]<=tar:
                w =  dp[idx][tar-denm[idx]]
            dp[idx][tar] = w+wo
    return dp[n-1][target]



def countWaysToMakeChange(denm, value) :
    
	# Your code goes here
    n = len(denm)
#     res = f_rec(denm,n-1,value)
#     dp = [[-1]*(value+1) for _ in range(n)]
#     res = f_mem(denm,n-1,value,dp)

    res = f_tab(denm,value,n)
    
    return res































#taking inpit using fast I/O
def takeInput() :
    numDenominations = int(input())

    denominations = list(map(int, stdin.readline().strip().split(" ")))

    value = int(input())
    return denominations, numDenominations, value


#main
denominations, numDenomination, value = takeInput()
print((countWaysToMakeChange(denominations, value)))