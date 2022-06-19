class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        zero_count = 0
        two_count = 0
        for idx,n in enumerate(nums):
            if n==0:
                zero_count+=1
            elif n==2:
                two_count+=1
        one_count = len(nums) - (zero_count+two_count)
        nums[:] = [0]*zero_count + [1]*one_count + [2]*two_count
        
            