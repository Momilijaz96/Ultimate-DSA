class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        fmap = {}
        for idx,n in enumerate(nums):
            if n not in fmap:
                fmap[n] = ([idx],target - n)
            else:
                fmap[n][0].append(idx)
        
        res = []
        for k in fmap:
            if fmap[k][1] in fmap and fmap[k][1]!=k:
                for idx in fmap[k][0]:
                    res.append(idx)
                for idx in fmap[fmap[k][1]][0]:
                    res.append(idx)
            elif fmap[k][1] in fmap and fmap[k][1]==k:
                if len(fmap[k][0])>1:
                    res+=fmap[k][0]
                    
        res = list(set(res))
        return res