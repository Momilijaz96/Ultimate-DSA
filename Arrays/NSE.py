def nextSmallerElement(arr,n):
    # Write your code here.
    res = []
    dic = {}
    dic[-1] = [-1,-1]
    idx = -1
    res = [-1]
    while(idx > -1*(n)):
        idx-=1
        if arr[idx] > arr[idx+1]:
            dic[idx] = [idx+1,arr[idx+1]]
            res.insert(0,arr[idx+1])
        elif arr[idx] < arr[idx+1]:
            next = dic[idx+1]
            while(arr[idx]<=next[1]):
                next = dic[next[0]]
            dic[idx] = next
            res.insert(0,next[1])
        else:
            dic[idx] = dic[idx+1]
            res.insert(0,dic[idx+1][1])
        #print(dic)
    return res