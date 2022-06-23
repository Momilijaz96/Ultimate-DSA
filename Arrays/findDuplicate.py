import math
import numpy as np
import cmath

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    fmap = {}
    for a in arr:
        if a not in fmap:
            fmap[a] = 1
        else:
            return a


    

