from os import *
from sys import *
from collections import *
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def pairSum(arr, s):
    # Write your code here.
    res = []
    arr.sort()
    slow = 0
    fast = len(arr)-1
    #print(arr)
    while(slow<fast):
        mysum = arr[slow]+arr[fast]
        if mysum==s:
            res.append([arr[slow],arr[fast]])
            if arr[fast]==arr[slow]:
                n = fast-slow
                count = int( nCr(n+1,2) - 1)
                res+= [(arr[fast],arr[fast])]*count
                break
            if arr[fast]==arr[fast-1] or arr[slow]==arr[slow+1]:
                fc=1
                sc=1
                while arr[fast]==arr[fast-1] or arr[slow]==arr[slow+1]:
                    if arr[fast]==arr[fast-1]: 
                        fc+=1
                        fast-=1
                    if arr[slow]==arr[slow+1]: 
                        sc+=1
                        slow+=1
                count = fc*sc
                temp = [(arr[slow],arr[fast])] * (count-2)
                res+=temp
                
            elif arr[fast-1]==arr[fast]:
                fast-=1
            elif arr[slow+1]==arr[slow]:
                slow+=1   
            else:
                slow+=1
        elif mysum<s:
            slow+=1
        elif mysum>s:
            fast-=1
    return res
                