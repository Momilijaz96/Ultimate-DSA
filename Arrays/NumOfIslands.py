def eight_conn(i,j,m,n):
    i_back = i-1
    i_forw = i+1
    j_back = j-1
    j_forw = j+1
    if i_back<0: i_back=0
    if i_forw>m-1: i_forw=m-1
    if j_back<0: j_back=0
    if j_forw>n-1: j_forw=n-1
    
    return [(i_back,j_back),
           (i,j_back),
           (i_forw,j_back),
           (i_forw,j),
           (i_forw,j_forw),
           (i,j_forw),
           (i_back,j_forw),
           (i_back,j)]
    
def make_island(mat,i,j,m,n,res):
    #print(i,j)
    res+=1
    mat[i][j]=-1
    eight_idx = eight_conn(i,j,m,n)
    eight_idx = list(set(eight_idx))
    #print(eight_idx)
    for idx in eight_idx:
        a,b = idx
        #print(a,b)
        if mat[a][b]==1:
            res = make_island(mat,a,b,m,n,res)
    return res
    
def findIslands(mat,m,n):
	# Your code goes here.
    res = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j]==1:
                island = 0
                island = make_island(mat,i,j,m,n,island)
                if island>0:
                    res+=1
                    
    return res
                    