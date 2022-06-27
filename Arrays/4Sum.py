from os import *
from sys import *
from collections import *
from math import *

def fourSum(arr, target):
    # Write your code here
    if len(arr)==4:
        if sum(arr)==target: return "Yes"
        else: return "No" 

    
    n = len(arr)
    smap = {}
    for i in range(n):
        for j in range(i+1,n):
            s = arr[i]+arr[j]
            rem = target - s
            idx = [i,j]
            if s not in smap:
                smap[s] = [rem,idx]
            else:
                smap[s][1]+=[i,j]
    #print(sum)
    for k in smap:
        if smap[k][0] in smap:
            if (target - k) == k:
                if len(smap[k][1])>2:
                    return "Yes"
            else:
                    return "Yes"
    return "No"
            
            
            
    
    
    
    