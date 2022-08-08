from os import *
from sys import *
from collections import *
from math import *
import heapq
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :
    zc = 0
    tc = 0
    for idx in range(n):
        if arr[idx]==0: zc+=1
        elif arr[idx]==2: tc+=1
    oc = n - (zc+tc)
    arr[:zc] = [0]*zc
    arr[zc:oc] = [1]*oc
    arr[oc:] = [2]*tc
    return arr
    
#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
