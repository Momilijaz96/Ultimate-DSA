def removeDuplicates(arr,n):
    # Write your code here.
    i = 1
    while(i<len(arr)):
        if arr[i]==arr[i-1]:
            arr.pop(i)
        else:
            i+=1
    return len(arr)