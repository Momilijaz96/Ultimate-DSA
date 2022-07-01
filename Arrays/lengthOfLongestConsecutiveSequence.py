from os import *
from sys import *
from collections import *
from math import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    seq_map = {}
    for k in arr:
        if k not in seq_map:
            seq_map[k] = 0
    res = 1
    cur_seq = 0
    idx = arr[0]
    count = 0
    n = len(arr)
    for i in seq_map:
        if seq_map[i]==0:
            idx = i
            while(idx in seq_map):
                cur_seq += 1
                seq_map[idx] = 1
                idx = idx+1
                
            res = max(res,cur_seq)
            cur_seq = 0
    return res

