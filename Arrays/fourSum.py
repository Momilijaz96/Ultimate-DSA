from os import *
from sys import *
from collections import *
from math import *

def PairSum(nums,traget):
    fmap = {}
    for idx,n in enumerate(nums):
        if n not in fmap:
            fmap[n] = ([idx],target - n)
        else:
            fmap[n][0].append(idx)
    
    res = []
    for k in fmap:
        if fmap[k][1] in fmap and fmap[k][1]!=k:
            for idx in fmap[k][0]:
                res.append(idx)
            for idx in fmap[fmap[k][1]][0]:
                res.append(idx)
        elif fmap[k][1] in fmap and fmap[k][1]==k:
            if len(fmap[k][0])>1:
                res+=fmap[k][0]
                    
    res = list(set(res))
    return res

def fourSum(arr, target):
    # Write your code here
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            a = arr[i]
            b = arr[j]
            rem = target - (a+b)
            res = PairSum(arr[j+1:],rem)
            if len(res)>0:
                return "Yes"
    return "No"
            
            
    