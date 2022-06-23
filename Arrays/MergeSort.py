def split(arr):
    n = len(arr)
    if n==1:
        return arr
    mid = n//2
    return arr[:mid],arr[mid:]

def merge(arr1,arr2):

    for a in arr1:
        if a<    