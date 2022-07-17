class listy:
    def __init__(self, l):
        self.values = l

    def elementAt(self,i):
        if i<len(self.values):
            return self.values[i]
        else:
            return -1

def binary_search(x,listy,start,end):
    mid = (start+end)//2
    if listy.elementAt(mid)==x:
        return mid
    elif start==mid or end==mid:
        return -1
    elif x<listy.elementAt(mid):
        return binary_search(x,listy,start,mid)
    else:
        return binary_search(x,listy,mid,end)

def find_x(x,listy):
    #Find size
    i = 1
    while(listy.elementAt(i)>0):
        i*=2
    size = i//2
    idx = -1
    if x>=listy.elementAt(size):
        i = size
        while(listy.elementAt(i)>0):
            if listy.elementAt(i)==x:
                idx = i
                break
            i+=1
    else:
        idx = binary_search(x,listy,0,size)
    return idx


l = listy([1, 3,5, 8,10,10,15,27,92])
res = find_x(100, l)
print(res)