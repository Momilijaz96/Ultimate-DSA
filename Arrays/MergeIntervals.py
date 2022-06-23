import numpy as np
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        idx = 0
        count = 0
        
        #Sort by lower bound
        intervals.sort(key=lambda tup: tup[0])
        
        while(idx<len(intervals)-1):
            n = len(intervals)-1
            if intervals[idx][1]>=intervals[idx+1][0] and intervals[idx][0]<=intervals[idx+1][1]:
                intervals[idx][1] = max(intervals[idx][1],intervals[idx+1][1])
                intervals[idx][0] = min(intervals[idx][0],intervals[idx+1][0])
                x = intervals.pop(idx+1)
            else:
                idx +=1                
        return intervals
    