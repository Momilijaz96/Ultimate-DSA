from itertools import combinations

def findSubsetsThatSumToK(arr, n, k) :
    # Write your code here.
    res = []
    r = n
    while(r>0):
        temp = list(combinations(arr,r))
        for l in temp:
            if sum(l)==k: res.append(l)
        r-=1
    return res