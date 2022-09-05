import sys
sys.setrecursionlimit(10**7)

def f_recur(grid,x,y):
    if x==0 and y==0:
        return grid[x][y]
    if x<0 or y<0: return float('inf')
    top =  f_recur(grid,x-1,y)
    left =  f_recur(grid,x,y-1)
    return grid[x][y] + min(top,left)

def f_mem(grid,x,y,dp):
    if x==0 and y==0:
        return grid[x][y]
    if x<0 or y<0: return float('inf')
    if dp[x][y]==-1:
        top =  f_mem(grid,x-1,y,dp)
        left =  f_mem(grid,x,y-1,dp)
        dp[x][y] = grid[x][y] + min(top,left)
    return dp[x][y]

def f_tab(grid,m,n):
    dp = [[float('inf')]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(m):
        for j in range(n):
            if i+1<m:
                dp[i+1][j] = min(dp[i+1][j], grid[i+1][j]+dp[i][j])
            if j+1<n:
                dp[i][j+1] = min(dp[i][j+1], grid[i][j+1]+dp[i][j])
    return dp[-1][-1]


def f_sp(grid,m,n):
    row = [float('inf')]*n
    row[0] = grid[0][0]
    for i in range(m):
        next_row = [float('inf')]*n
        for j in range(n):
            if i+1<m:
                next_row[j] = min(next_row[j], grid[i+1][j]+row[j])
            if j+1<n:
                row[j+1] = min(row[j+1], grid[i][j+1]+row[j])
        if i<m-1:
            row = next_row.copy()
    return row[-1]
            

def minSumPath(grid):
    # Write your code here.
    m = len(grid)
    n = len(grid[0])
#     res = f_recur(grid,m-1,n-1)
    
    # Memoization
#     dp = [[-1]*n for _ in range(m)]
#     res = f_mem(grid,m-1,n-1,dp)
   
    # Tabulation
#     res = f_tab(grid,m,n)     

    # Space Optimization
    res = f_sp(grid,m,n)
    return res



# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n,m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(grid))
    t -= 1