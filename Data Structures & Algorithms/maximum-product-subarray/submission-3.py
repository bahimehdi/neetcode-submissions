class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = minProd = maxProd = nums[0]

        for i in range(1, len(nums)):
            Min = minProd * nums[i]
            Max = maxProd * nums[i]
            minProd, maxProd = min(nums[i], Min, Max), max(nums[i], Min, Max)
            globalMax = max(globalMax, maxProd)

        return globalMax