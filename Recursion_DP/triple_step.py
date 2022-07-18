def my_steps(n, memo):
    if n==1 or n==2:
        return n
    elif n==3:
        return 4
    if memo[n]==0:
        memo[n] = my_steps(n-1,memo) + my_steps(n-2,memo) + my_steps(n-3,memo) 
    return memo[n]

n = 5
memo = [0 for i in range(n+1)]
print(my_steps(n, memo))