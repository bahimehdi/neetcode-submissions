# nums = array of int
# target = nums[i] + nums[j] and i!=j
# there is a single pair = target, return their index in a list (just return the first pair)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for i, num in enumerate(nums):
            if num not in needed:
                needed[target - num] = i
            else:
                return [needed[num], i]