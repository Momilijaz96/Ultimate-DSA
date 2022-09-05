def f_recur(triangle,n,x,y):
    if x>n-1 or y>x:
        return float('inf')
    if x==n-1:
        return triangle[x][y]
    btm = f_recur(triangle,n,x+1,y)
    btm_rit = f_recur(triangle,n,x+1,y+1)
    return triangle[x][y] + min(btm,btm_rit)
  
def f_mem(arr,n,x,y,dp):
    if x>n-1 or y>x:
        return float('inf')
    if x==n-1:
        return arr[x][y]
    if dp[x][y]==float('inf'):
        btm = f_mem(arr,n,x+1,y,dp)
        btm_rit = f_mem(arr,n,x+1,y+1,dp)
        dp[x][y] = arr[x][y] + min(btm,btm_rit)
    return dp[x][y]
    
def f_tab(arr,n):
    dp = [[float('inf')]*i for i in range(1,n+1)]
    dp[0][0] = arr[0][0]
    for i in range(1,n):
        for j in range(i+1):
            dp[i][j] = arr[i][j] 
            top = dp[i-1][j] if (i-1>=0 and j<=i-1) else float('inf')
            top_left = dp[i-1][j-1] if (i-1>=0 and j-1>=0) else float('inf')
            dp[i][j] += min(top,top_left)
    return min(dp[-1])

def f_sp(arr,n):
    row = [arr[0][0]]
    for i in range(1,n):
        next_row = [float('inf')]* (i+1)
        for j in range(i+1):
            next_row[j] = arr[i][j]
            top = row[j] if (i-1>=0 and j<=i-1) else float('inf')
            top_left = row[j-1] if (i-1>=0 and j-1>=0) else float('inf')
            next_row[j] += min(top,top_left)
        row = next_row.copy()
    return min(row)

def minimumPathSum(triangle, n):
    # Write your code here.
#     res = f_recur(triangle,n,0,0)
    
    # Memoization
#     dp = [[float('inf')]*i for i in range(1,n+1)]
#     res = f_mem(triangle,n,0,0,dp)

    # Tabulation
#     res = f_tab(triangle,n)

    # Space Optimization
    res = f_sp(triangle,n)
    return res