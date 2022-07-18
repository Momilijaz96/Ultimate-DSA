def multiply(a,b,memo):

    if a > b: x, m = a, b
    else: x, m = b, a

    if m==2:
        return x + x
    if m == 0:
        return 0
    if (m,x) not in memo:
        if m%2 == 0:
            memo[(m,x)] = multiply(m//2, x, memo) + multiply(m//2, x, memo) 
        else:

            memo[(m,x)] =  multiply(m//2, x, memo) + multiply(m//2, x, memo) + x

    return memo[(m,x)]
memo = {}
print(multiply(24,26,memo))
print(memo)