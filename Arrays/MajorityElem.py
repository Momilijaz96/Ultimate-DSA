from os import *
from sys import *
from collections import *
from math import *

def findMajorityElement(arr, n):
    # Write your code here.
    fmap = {}
    count = math.floor(n/2) 
    for k in arr:
        if k not in fmap:
            fmap[k] = 1
        else:
            fmap[k]==1
        if fmap[k] == count:
            return k