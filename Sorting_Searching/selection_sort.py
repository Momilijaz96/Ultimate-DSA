import numpy as np
def selection_sort(arr):
    n = len(arr)
    count = 0
    while(count<n):
        idx = np.argmin(arr[count:])
        min = arr.pop(idx+count)
        arr.insert(count,min)
        count+=1
    return arr    

x = [5,4,3,2,1]
print(selection_sort(x))