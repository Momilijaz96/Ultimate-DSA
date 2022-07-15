def ninjaAndLadoos(row1, row2, m, n, k):
    # Write your code here.
    r1 = 0
    r2 = 0
    count = 0
    res = 0
    while(count<k):
        if len(row1)>0 and len(row2)>0:
            if row1[0]<row2[0]:
                res = row1.pop(0)
            else:
                res = row2.pop(0)
        elif len(row1)==0 and len(row2)==0:
            break
        elif len(row1)==0:
            res = row2.pop(0)
        else:
            res = row1.pop(0)
        count+=1
    return res
