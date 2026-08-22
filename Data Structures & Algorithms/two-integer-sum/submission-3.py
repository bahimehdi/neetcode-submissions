# nums = array of int
# target = nums[i] + nums[j] and i!=j
# there is a single pair = target, return their index in a list

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = list(enumerate(nums))
        sorted_pairs = sorted(indexed, key = lambda x:x[1])
        i = -1
        j = 0
        high = sorted_pairs[i]
        low = sorted_pairs[j]
        while high[1] >= low[1]:
            if target == high[1] + low[1]:
                if high[0] >= low[0]:
                    return [low[0], high[0]]
                else:
                    return [high[0], low[0]]
            elif target < high[1] + low[1]:
                i -= 1
                high = sorted_pairs[i]
            elif target > high[1] + low[1]:
                j += 1
                low = sorted_pairs[j]