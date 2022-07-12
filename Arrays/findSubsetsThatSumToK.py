from itertools import combinations

def get_comb(arr,subset,res):
    if len(arr)==0:
        return res
    s_w = subset + [arr[0]]
    s_wo = subset
    res.append(s_w)
    res = get_comb(arr[1:],s_w,res)
    res = get_comb(arr[1:],s_wo,res)
    return res

def findSubsetsThatSumToK(arr, n, k) :
    # Write your code here.
    res = []
    r = n
    combs = get_comb(arr,[],[])
    for c in combs:
        if sum(c)==k:
            res.append(c)
    return res
    
    
       