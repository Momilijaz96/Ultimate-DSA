def quick_sort(arr):
    n = len(arr)
    if len(arr)==0 or len(arr)==1:
        return arr
    mid = n//2
    p1 = []
    p2 = []
    pivot = arr[mid]
    for i in range(n):
        if i==mid: continue
        if arr[i]<pivot:
            p1.append(arr[i])
        else:
           p2.append(arr[i])
    lh = quick_sort(p1)
    rh = quick_sort(p2)
    return lh+[pivot]+rh
        
x = [5,4,3,2,1]
print(quick_sort(x))