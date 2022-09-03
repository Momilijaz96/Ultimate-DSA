from sys import stdin
def all_subsets(nums,i,cs,ms,dp):
    if i==0:
        return nums[0]
    if i<0:
        return 0
    if dp[i]==-1:
        ws = nums[i] + all_subsets(nums,i-2,cs,ms,dp)
        wos = all_subsets(nums,i-1,cs,ms,dp)
        dp[i] = max([ws,wos,ms])
    return dp[i]

def tab_all_subsets(nums):
    n = len(nums)
    a = nums[0]
    b = a
    if n>1:
        b = max(nums[0],nums[1])
        for i in range(2,n):
            temp = max(b , a+nums[i])
            a = b
            b = temp
#     print(dp)
    return b

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp = [-1]*len(nums)
#     res = all_subsets(nums,len(nums)-1,0,0,dp)
    res = tab_all_subsets(nums)
    return res

# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1