def merge_pair(a,b):
    res = []
    while(len(a)>0 and len(b)>0):
        if a[0]<b[0]:
            res.append(a.pop(0))
        elif a[0]>=b[0]:
            res.append(b.pop(0))
    if len(a)>0:
        res += a
    elif len(b)>0:
        res+= b
    return res

def mergeKSortedArrays(kArrays, k:int):
    # Write your code here.
    # kArrays is a list of 'k' lists.
    # Return a list.
    res = kArrays[0]
    for arr in kArrays[1:]:
        res = merge_pair(res,arr)
    return res