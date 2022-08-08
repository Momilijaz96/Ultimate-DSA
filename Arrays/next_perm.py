from os import *
from sys import *
from collections import *
from math import *
import heapq

def minimal_max(k,arr,offset):
    h = arr.copy()
    h = [(arr[i],i+offset) for i in range(len(h))]
    heapq.heapify(h)
    m = heapq.heappop(h)
    while(m[0]<k):
        m = heapq.heappop(h)
    return m[0],m[1] #elem,idx

def nextPermutation(permutation, n):
    # Write your code here.
    # Return a list.
    i = n-1
    while(i>-1):
        if permutation[i]<permutation[i-1]: 
            pass
        else:    
            mx,mx_idx = minimal_max(permutation[i-1],permutation[i:],i)
            permutation[mx_idx],permutation[i-1] = permutation[i-1],permutation[mx_idx]
            permutation[i:] = sorted(permutation[i:])
            break
        i-=1
    return permutation
            
            
            
            
            
            
            
