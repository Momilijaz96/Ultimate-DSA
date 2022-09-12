from typing import List

def f_sp(arr,n,tar):
    prev_row =  [0]*(tar+1)
    if arr[0]==0:
        prev_row[0] = 2
    else:
        prev_row[0] = 1
    if arr[0]<=tar and arr[0]!=0:
        prev_row[arr[0]] = 1
    for idx in range(1,n):
        row =  [0]*(tar+1)
        for ctar in range(tar+1):
            w = 0
            if arr[idx]<=ctar:
                w = prev_row[ctar-arr[idx]]
            wo = prev_row[ctar]
            row[ctar] = w+wo
        prev_row = row
    return prev_row[tar]

def targetSum(arr: List[int], d: int) -> int:
    s = sum(arr)
    n = len(arr)
    if (d+s)%2>0:
        return 0
    tar = (d+s)//2
    res = f_sp(arr,n,tar)
    return res 