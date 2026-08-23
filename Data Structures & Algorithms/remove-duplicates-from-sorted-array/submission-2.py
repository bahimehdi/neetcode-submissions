# Ascending order list
# task: remove dups, return nums with no dups

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = k = 0
        while l < len(nums):
            used = nums[l]
            while l < len(nums) and nums[l] == used:
                l += 1
            nums[k] = used
            k += 1
        return k