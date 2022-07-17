
def is_perm(s1, s2):
    d = {}
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 0
    
    for i in s2:
        if i in d:
            if d[i] > 0:
                d[i] -=1
            else:
                return False
        else:
            return False
    for key in d:
        if d[key] > 0:
            return False
    return True

def group_anagrams(strs):
    n = len(strs)
    d = {}
    for i in range(n):
        l = list(strs[i])
        l.sort()
        sorted = "".join(l)
        if  sorted not in d:
            d[sorted] = [strs[i]]
        else:
            d[sorted].append(strs[i])
    
    return list(d.values())

            
strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(strs))