class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        s = 0
        n = len(nums)
        for i in range(n):
            mn = nums[i]
            mx = nums[i]
            for j in range(i+1, n):
                mx = max(mx,nums[j])
                mn = min(mn,nums[j])
                s += mx - mn
        return s