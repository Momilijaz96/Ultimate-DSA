class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        n = len(nums)
        max_sum=0
        idx = 0
        while(idx<n):
            cur_sum=0
            while(idx<n and nums[idx]):
                cur_sum+=1
                idx+=1
            max_sum = max(max_sum,cur_sum)
            idx+=1
        return max_sum
                