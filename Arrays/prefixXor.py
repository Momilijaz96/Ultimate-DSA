from os import *
from sys import *
from collections import *
from math import *

def subarraysXor(arr, x):
    # Write your code here
    # Return an integer
    res = 0
    n = len(arr)
    preXor = {}
    preXor[0]=1
    xor = 0
    for e in arr:
        xor = xor^e
        req = xor^x
        res+=preXor.get(req,0)
        preXor[xor] = preXor.get(xor,0) + 1    
       
    return res  
