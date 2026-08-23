# Ascending order list
# task: remove dups, return nums with no dups

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        k = 0
        while l < r:
            used = nums[l]
            while l < r and nums[l] == used:
                l += 1
                nums[k] = used
            k += 1
        return k