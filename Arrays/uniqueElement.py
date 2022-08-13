def uniqueElement(arr, n):
    # Write your code here
    idx = 0
    res = 0
    while(idx<n-1):
        if arr[idx]==arr[idx+1]:
            idx+=2
        else:
            res = arr[idx]
            idx+=1
    if idx==n-1:
        res=arr[-1]
    return res
            

