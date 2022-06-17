class Solution:
    
    def swap(self, idx_a, idx_b, nums):
        temp = nums[idx_a]
        nums[idx_a] = nums[idx_b]
        nums[idx_b] = temp
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0: return []
        if n == 1: return nums
        dc = -1
        for i in range(n-1, 0, -1):
            if (nums[i] > nums[i-1]) and (dc==-1):
                return self.swap(i, i-1, nums)
            elif (nums[i] > nums[i-1]) and (dc!=-1):
                break
            elif nums[i] <= nums[i-1]:
                dc = i-1
                
        if dc==0:
            nums.sort()
        
        new_stage = nums[dc:][0]
        new_stage_idx = dc 
        stg = nums[dc-1]
        stg_idx = dc-1
        
        for i, k in enumerate(nums[dc:]):
            if k < new_stage and k > stg:
                new_stage = k
                new_stage_idx = i + dc
        
        self.swap(stg_idx, new_stage_idx, nums)
        copy = nums[dc:]
        copy.sort()
        nums[dc:] = copy
       
    