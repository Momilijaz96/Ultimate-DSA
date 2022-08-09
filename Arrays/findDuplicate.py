import math
import numpy as np
import cmath

def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    idx = 0
    while(idx<n):
        if arr[idx]==-1:
            return idx
        new_idx = arr[idx] 
        arr[idx] = -1
        idx = new_idx
        


    

