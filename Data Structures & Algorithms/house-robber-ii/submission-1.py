# dp[i] means:
# base cases: 
# how state is calculated:
# the answer:

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        return max(self.HouseRobber1(nums[1:]), self.HouseRobber1(nums[:-1]))
    
    def HouseRobber1(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 3:
            return max(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]