# - input
# nums: array of int
# - output
# peakIndex: index of any of the peaks (index of the first peak you find)
# - glossary
# a peak element is element strictly greater than its neighbors

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n - 1
        while L < R:
            M = (L + R) // 2
            if nums[M] < nums[M + 1]:
                L = M + 1
            elif nums[M] < nums[M - 1]:
                R = M - 1
            else:
                return M
        return L