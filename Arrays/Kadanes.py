class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums)==1: return nums[0]
        
        max_sum = nums[0]
        cum_sum = 0
        start = 0
        end = 0
        
        for idx,n in enumerate(nums):
            print(cum_sum,max_sum,start,end)
            cum_sum += n
            if cum_sum > max_sum:
                max_sum = cum_sum
                end = idx+1
            if cum_sum<0:
                start = idx+1
                cum_sum = 0
            
        return max_sum
    