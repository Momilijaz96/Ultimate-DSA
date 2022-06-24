from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit


def findTriplets(nums, x, k):
    nums.sort()
    res = []
    for idx,n in enumerate(nums):
        slow = idx+1
        fast = len(nums)-1
        while(slow<fast):
            if nums[slow]+nums[fast]+n==k:
                    #print(slow,fast,idx)
                    temp = (nums[slow],nums[fast],n)
                    res.append((temp))
            if nums[slow]+nums[fast] < k-n:
                slow+=1
            else:
                fast-=1
                
    res = list(set(res))
    res = list(map(list,res))
    return res
            
            
#Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
