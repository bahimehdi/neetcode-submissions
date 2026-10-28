class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = nums[0]
        minProd = maxProd = nums[0]

        for i in range(1, len(nums)):
            minProd, maxProd = min(nums[i], minProd * nums[i], maxProd * nums[i]), max(nums[i], maxProd * nums[i], minProd * nums[i])
            globalMax = max(globalMax, maxProd)

        return globalMax