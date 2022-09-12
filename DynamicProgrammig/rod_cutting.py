from sys import stdin
import sys
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


def cutRod(price, n):

    # Write your code here.
    wts = [i for i in range(1,n+1)]
    res = f_tab(n-1,n,price,wts)
    return res
# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
