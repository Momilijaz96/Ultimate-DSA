def longestSubSeg(arr, n, k):
    max_ones = 0
    zero_flip = k
    for i in range(n):
        count = 0
        k = zero_flip
        for j in range(i,n):
            if arr[j]==1: 
                count+=1
            elif k>0:
                k-=1
                count+=1
            else:
                max_ones = max(max_ones,count)
                count = 0
        max_ones = max(max_ones,count)
    return max_ones

        