#0 1 1 2 3 5 
def fib(n):
    a,b = 0,1
    for i in range(2,n+1):
        t = a+b
        a,b = b,t
    return t

print(fib(5))