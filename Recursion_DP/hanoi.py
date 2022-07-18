import numpy as np
def hanoi(n,towers,res):
    if n==2:
        return [[1,2],[1,3],[2,3]]
    if n<towers[1][-1]:
        towers[1].append(n)
        res.append([1,2])
        towers[0].pop(-1)
    elif n>towers[2][-1]:
        towers[2].append(n)
        res.append([1,3])
        towers[0].pop(-1)
    else:
        idx = np.argmin([towers[1][-1],towers[2][-1]])
        top = towers[idx+1].pop(-1)
        towers[idx].append(top)
        res.append([idx+1,idx])
    return hanoi(n-1,towers,res)

def towerOfHanoi(n):
    res = []
    towers = [[],[-1],[-1]]
    towers[0] = [i for i in range(1,n)]
    return hanoi(n,towers,res)
