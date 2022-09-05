from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

def f_recur(arr,x,y,m,n):
    if x>m-1 or y>n-1 or y<0:
        return float('-inf')
    if x==m-1:
        return arr[x][y]
    btm_left = f_recur(arr,x+1,y-1,m,n)
    btm = f_recur(arr,x+1,y,m,n)
    btm_rit = f_recur(arr,x+1,y+1,m,n)
    return arr[x][y] + max(btm_left,btm,btm_rit)

def f_mem(arr,x,y,m,n,dp):
    if x>m-1 or y>n-1 or y<0:
        return float('-inf')
    if x==m-1:
        return arr[x][y]
    if dp[x][y]==float('-inf'):
        btm_left = f_mem(arr,x+1,y-1,m,n,dp)
        btm = f_mem(arr,x+1,y,m,n,dp)
        btm_rit = f_mem(arr,x+1,y+1,m,n,dp)
        dp[x][y] = arr[x][y] + max(btm_left,btm,btm_rit) 
    return dp[x][y]

def f_tab(arr,m,n):
    dp = [[float('-inf')]*n for _ in range(m)]
    dp[0] = arr[0]
    for i in range(1,m):
        for j in range(n):
            dp[i][j] = arr[i][j]
            top_left = dp[i-1][j] if (i-1>=0) else float('-inf')
            top = dp[i-1][j-1] if (i-1>=0 and j-1>=0) else float('-inf')
            top_rit = dp[i-1][j+1] if (i-1>=0 and j+1<=n-1) else float('-inf')
            dp[i][j] += max(top,top_left,top_rit)
    return max(dp[-1])

def f_sp(arr,m,n):
    prev_row = arr[0]
    for i in range(1,m):
        row = [0]*n
        for j in range(n):
            row[j] = arr[i][j]
            top_left = prev_row[j] if (i-1>=0) else float('-inf')
            top = prev_row[j-1] if (i-1>=0 and j-1>=0) else float('-inf')
            top_rit = prev_row[j+1] if (i-1>=0 and j+1<=n-1) else float('-inf')
            row[j] += max(top,top_left,top_rit)
            
        prev_row = row.copy()
    return max(prev_row)

def getMaxPathSum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    #   Write your code here
#     res = float('-inf')
#     dp = [[float('-inf')]*n for _ in range(m)]
    
#     for s in range(n):
        #res = max(res,f_recur(matrix,0,s,m,n))
#         res = max(res,f_mem(matrix,0,s,m,n,dp))

    # Tabulation
#     res = f_tab(matrix,m,n)
    #Space Optimization
    res = f_sp(matrix,m,n)
    return res

























#   taking inpit using fast I/O
def takeInput() :
    n_x = stdin.readline().strip().split(" ")
    n = int(n_x[0].strip())
    m = int(n_x[1].strip())

    matrix=[list(map(int, stdin.readline().strip().split(" "))) for row in range(n)]

    return matrix, n, m


#   main
T = int(input())
while (T > 0):
    T -= 1
    matrix, n, m = takeInput()
    print(getMaxPathSum(matrix))
