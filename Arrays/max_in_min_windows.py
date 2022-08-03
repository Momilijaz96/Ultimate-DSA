def min_in_window_k(arr,k):
    if k==1: 
        return arr
    elif k==len(arr):
        return [min(arr)]
    res = []
    dq = []
    st = 0
    end = st
    n = len(arr)
    while(end<n):
        if len(dq)==0 or dq[-1]>arr[end]:
            while(dq and arr[end]<dq[-1]):
                dq.pop()
            dq.append(arr[end])
        else: #top of dequeue has smaller elems - put this one from end.
            if arr[end]>dq[0]:
                dq.insert(0,arr[end])
            else:
                while(dq and arr[end]<dq[0]):
                    dq.pop(0)
                dq.insert(0,arr[end])
        if len(arr[st:end+1])==k:
            res.append(dq[-1])
            if dq[-1]==arr[st]:
                dq.pop()
            st+=1
            end+=1
        else:
            end+=1
    return res  
            
            
def maxMinWindow(arr,n):
    # Write your code here
    # Return a list of integers
    res = []
    for k in range(1,n+1):
        mins = min_in_window_k(arr,k)
        #print(k,mins)
        res.append(max(mins))
    return res
    
    