def f_recur(x,y,mat):
    if x==0 and y==0:
        return 1
    if x<0 or y<0 or mat[x][y]==-1:
        return 0

    top = f_recur(x-1,y,mat)
    left = f_recur(x,y-1,mat)
    return top+left

def f_mem(x,y,mat,dp):
    if x==0 and y==0:
        return 1
    if x<0 or y<0 or mat[x][y]==-1:
        return 0
    if dp[x][y]==-1:
        top = f_mem(x-1,y,mat,dp)
        left = f_mem(x,y-1,mat,dp)
        dp[x][y] = top+left
    return dp[x][y]

def f_tab(m,n,mat):
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if mat[i][j]!=-1:
                if i+1<m:
                    dp[i+1][j] += dp[i][j]
                if j+1<n:
                    dp[i][j+1] += dp[i][j]
    return dp[-1][-1]

def f_sp(m,n,mat):
    row = [0]*n
    row[0] = 1
    next_row = row
    for i in range(m):
        row = next_row.copy()
        next_row = [0]*n
        for j in range(n):
            if mat[i][j]!=-1:
                if i+1<m:
                    next_row[j] += row[j]
                if j+1<n:
                    row[j+1] += row[j]
    return row[-1]

def mazeObstacles(m,n,mat):
    # Write your code here.
    mod_num = (10**9) + 7
#     res = f_recur(m-1,n-1,mat)
#     dp = [[-1]*n for _ in range(m)]
#     res = f_mem(m-1,n-1,mat,dp)
#     res = f_tab(m,n,mat)  
    res = f_sp(m,n,mat)
    return res%mod_num
    
