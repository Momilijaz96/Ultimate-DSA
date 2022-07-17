def get_pv(arr):
    n = len(arr)
    if n==1:
        return arr 
    i = 0 
    alt = -1
    while(i<n-1):
        if arr[i]-arr[i+1] >= 0 and (alt==-1 or alt==2):
            alt = -2
        elif arr[i]-arr[i+1] <= 0 and (alt==-1 or alt==-2):
            alt = 2
        else:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        i+=1
    return arr

arr = [5,8,6,2,3,4,6]
res = get_pv(arr)
print(res)