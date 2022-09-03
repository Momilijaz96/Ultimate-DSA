def all_subsets(nums,i,cs,dp):
    if i==0:
        return nums[0]
    if i<0:
        return 0
    if dp[i]==-1:
        ws = nums[i] + all_subsets(nums,i-2,cs,dp)
        wos = all_subsets(nums,i-1,cs,dp)
        dp[i] = max(ws,wos)
    return dp[i]

def houseRobber(nums):
    # Write your function here.
    n = len(nums)
    if n==1: return nums[0]
    dp = [-1]*(n-1)
    res1 = all_subsets(nums[:-1],len(nums)-2,0,dp)
    dp = [-1]*(n-1)
    res2 = all_subsets(nums[1:],len(nums)-2,0,dp)
    return max(res1,res2)