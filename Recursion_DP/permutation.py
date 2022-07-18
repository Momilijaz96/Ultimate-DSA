def perm(arr):
    if len(arr)==2:
        return [[arr[0],arr[1]],[arr[1],arr[0]]]
    top = arr[0]
    l = perm(arr[1:])
    res = []
    for p in l:
        for j in range(len(p)+1):
            temp = p[:]
            temp.insert(j,top)    
            res.append(temp)
    return res

x = [2,4,6,2]
print(len(perm(x)))