def frogJumpK(h,n,k):
    a = 0
    b = abs(h[1]-h[0])
    if n>2:
        for i in range(2,n):
            mins = abs(h[i]-h[i-1]) +a
            for j in range(2,k+1):
                if j<=i:
                    temp = abs( h[i] - h[i-j]) + b
                    mins = min(temp,mins)
            a,b = b,temp
    return b

h = [40,10,20,70,80,10,20,70,80,60]
h2 = [10,10]
h3 = [10,20,10]
print( frogJumpK(h3,len(h3),100) )
