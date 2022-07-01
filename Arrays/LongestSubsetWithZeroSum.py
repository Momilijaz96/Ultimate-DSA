def LongestSubsetWithZeroSum(arr):
    if sum(arr)==0: return len(arr)
    # Write your Code here.
    # Return an integer denoting the answer.
    smap = {arr[0]:0}
    n = len(arr)
    s = arr[0]
    res = 0
    for i in range(1,n):
        s += arr[i]

        if s not in smap:
            smap[s] = i
        else:
            res = max(res,(i - smap[s])) 
            smap[s] = min(smap[s],i)
            
        if s==0:
            #print(i)
            res = max(res,i+1)
            smap[s] = min(smap[s],i)
        
        
    return res


