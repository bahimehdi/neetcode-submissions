# The base case -> i == len(nums)
# Choices -> add nums[i], don't add nums[i]
# Constraints -> no dups
# Backtracking step -> pop the last number added

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(j, path)
        
        nums.sort()
        backtrack(0, [])
        return res