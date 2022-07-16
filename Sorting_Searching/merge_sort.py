import numpy as np
def merge_sort(arr):
    if len(arr)==1:
        return arr
    n = len(arr)
    mid = n//2
    lh = merge_sort(arr[:mid])
    rh = merge_sort(arr[mid:])
    return merge(lh,rh)

def merge(a,b):
    res = []
    while(a and b):
        if a[0]<b[0]:
            res.append(a.pop(0))
        elif a[0]>b[0]:
            res.append(b.pop(0))
        else:
            res.append(a.pop(0))
            res.append(b.pop(0))
    if len(a):
        res += a
    elif len(b):
        res += b
    return res

x = [5,4,3,2,1]
print(merge_sort(x))