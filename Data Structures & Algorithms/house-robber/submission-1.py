# - input: 
# nums: list<int>
# nums[i]: money on i'th house
# - constraint:
# cannot rob 2 adjascent houses (i-1,i,i+1)
# - output:
# max(nums[i] + nums[j] + nums[k] + ..); where i,j,k are not adjascent
# -> as in, i+1 < j, j+1 < k,..
# subproblem: max(nums[i-1], nums[i], nums[i+1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(dp[-1], dp[-2])