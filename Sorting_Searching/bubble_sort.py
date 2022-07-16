
def bubble_sort(arr):
    n = len(arr)
    count = 0
    while(count<n):
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        count+=1
    return arr    

x = [5,4,3,2,1]
print(bubble_sort(x))