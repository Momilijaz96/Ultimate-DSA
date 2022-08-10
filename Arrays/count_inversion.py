from os import *
from sys import *
from collections import *
from math import *


def merge_sort(arr):
    if len(arr)==1:
        return arr,0
    n = len(arr)
    mid = n//2
    l,linv = merge_sort(arr[:mid])
    r,rinv = merge_sort(arr[mid:])
    res,inv = merge(l,r,linv+rinv)
    return res,inv

def merge(arr1,arr2,inv=0):
    res = []
    while(len(arr1)>0 and len(arr2)>0):
        if arr1[0]<=arr2[0]:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))
            inv+=len(arr1)
    if len(arr1)>0:
        res += arr1
    else:
        res += arr2
    return res, inv

def getInversions(arr, n) :
    # Write your code here.
    res,inv = merge_sort(arr)

    return inv

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))