import heapq
def upd_pnt(p):
    p-=1
    if p<0:
        p=0
    return p

def kMaxSumCombination(a, b, n, k):
    # Write your code here.
    a.sort()
    b.sort()
    res = []
    pa = len(a)-1
    pb = len(b)-1
    keys = set()
    heap = [(-a[pa]-b[pb],pa,pb)]
    keys.add((pa,pb))
    heapq.heapify(heap)
    while(len(res) < k):
        sum,pa,pb = heapq.heappop(heap)
        res.append(sum*-1)
        print(pa,pb)
        if (upd_pnt(pa),pb) not in keys:
            heapq.heappush(heap,(-a[upd_pnt(pa)]-b[pb],upd_pnt(pa),pb))
            keys.add((upd_pnt(pa),pb))
        if (pa,upd_pnt(pb)) not in keys:
            heapq.heappush(heap,(-a[pa]-b[upd_pnt(pb)],pa,upd_pnt(pb)))
            keys.add((pa,upd_pnt(pb)))
    #print(keys)
    return res