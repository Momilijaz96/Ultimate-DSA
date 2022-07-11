import numpy as np
def maximumActivities(start, end):
    # Write your Code here.
    idx = np.argsort(end)
    end = [end[i] for i in idx]
    start = [start[i] for i in idx]
    count = 1
    curr_end = end[0]
    n = len(end)
   
    for i in range(1,n):
        if curr_end<=start[i]:
            count+=1
            curr_end = end[i]
    return count