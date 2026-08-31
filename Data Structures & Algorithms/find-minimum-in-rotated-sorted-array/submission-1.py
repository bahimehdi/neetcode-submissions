# - Input
# nums = sorted array in ascending order, rotated by k
# - Output
# find the k and return min(nums) in log(n)

# We need to rotate it until => while nums[L]] < nums[R]: n++
# with L starting at 0 and R starting at n - 1, then +1 -1
# then return nums[]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n - 1
        while L < R:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[R]:
                R = M
        return nums[L]