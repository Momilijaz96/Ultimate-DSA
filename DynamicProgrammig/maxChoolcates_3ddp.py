from typing import List

def f_recur(grid,r,c,x,y1,y2):
    if x>r-1 or y1<0 or y1>c-1 or y2<0 or y2>c-1:
        return float('-inf')
    if x==r-1:
        if y1==y2:
            return grid[x][y1]
        else:
            return grid[x][y1]+grid[x][y2]
    d = [-1,0,1]
    res = []
    for i in d:
        for j in d:
            res.append(f_recur(grid,r,c,x+1,y1+i,y2+j))
    if y1==y2:
        return grid[x][y1] + max(res)
    else:
        return grid[x][y1]+grid[x][y2]+max(res)
    
def f_mem(grid,r,c,x,y1,y2,dp):
    if x>r-1 or y1<0 or y1>c-1 or y2<0 or y2>c-1:
        return float('-inf')
    if x==r-1:
        if y1==y2:
            return grid[x][y1]
        else:
            return grid[x][y1]+grid[x][y2]
    if dp[y2][x][y1]==-1:
        d = [-1,0,1]
        maxi = float('-inf')
        for i in d:
            for j in d:
                maxi = max(maxi, (f_mem(grid,r,c,x+1,y1+i,y2+j,dp)) )
        if y1==y2:
            dp[y2][x][y1] = grid[x][y1] + maxi
        else:
            dp[y2][x][y1] = grid[x][y1]+grid[x][y2]+maxi
    return dp[y2][x][y1] #[y2]


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
#     res = f_recur(grid,r,c,0,0,c-1)
    
    # Memoization
    dp = [[[-1]*c for _ in range(r)] for _ in range(c)]
    res = f_mem(grid,r,c,0,0,c-1,dp)
    return res
  
    
