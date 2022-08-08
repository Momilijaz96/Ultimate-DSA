from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def msa(arr,idx,sum,n):
    if idx>n-1:
        return sum
   
    end = sum+arr[idx]
    st = msa(arr,idx+1,arr[idx],n)
    cont = msa(arr,idx+1,sum+arr[idx],n)
    #print(arr[idx],w,wo)
    return max(st,end,cont)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
	return max(0,msa(arr,0,0,n))































#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
