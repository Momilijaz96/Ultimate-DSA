def power_set(arr):
    res = []
    return subsets(arr, [], res)

def subsets(arr, subset, res):
    n = len(arr)
    if n == 0:
        return []
    s_w = subset + [arr[0]]
    res.append(s_w)
    subsets(arr[1:], s_w , res)
    subsets(arr[1:], subset, res)
    return res

print(power_set([2, 4, 6]))