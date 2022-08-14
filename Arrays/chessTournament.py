import numpy as np
def chessTournament(positions, n , c):
    positions.sort()
    min_ans = 0
    max_ans = max(positions) - min(positions)
    ans = np.arange(max_ans,min_ans,-1)
    idx = 0
    final_res = ans[idx]
    while(len(ans)>1):
        res = ans[idx]
        players = 1
        last_room = positions[0]
        for i in range(1,n):
            if positions[i]-last_room >= res:
                players += 1
                last_room = positions[i]
        if players >= c:
            final_ans = res
            ans = ans[:idx]
        else:
            ans = ans[idx:]
        idx = len(ans)//2
    return final_ans        
