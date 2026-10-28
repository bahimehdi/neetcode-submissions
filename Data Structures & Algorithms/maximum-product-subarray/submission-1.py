class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxdp = [float('-inf')] * n
        mindp = [float('inf')] * n
        maxdp[0] = nums[0]
        mindp[0] = nums[0]
        globalMax = nums[0]

        for i in range(1, n):
            mindp[i] = min(nums[i], maxdp[i-1] * nums[i], mindp[i-1] * nums[i])
            maxdp[i] = max(nums[i], maxdp[i-1] * nums[i], mindp[i-1] * nums[i])
            globalMax = max(globalMax, maxdp[i])
        return max(maxdp)