import numpy as np
def ayushGivesNinjatest(n, m, time):
    
    # Write your code here.
    min_ans = max(time)
    max_ans = sum(time)
    ans = np.arange(min_ans,max_ans+1)
    idx = 0
    res = min_ans
    while(len(ans)>1):
        cur_sum = 0
        days = 1 
        for i in range(m):
            cur_sum += time[i]
            if cur_sum>res:
                cur_sum=time[i]
                days+=1
        if days<=n:
            res = ans[idx]
            ans = ans[:idx]
        else:
            ans = ans[idx:]
        idx = len(ans)//2
    return res


