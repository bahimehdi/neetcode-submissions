# The base case -> sum(path) == target
# Choices -> recurse with nums[i], recurse with nums[i+1]
# Constraints -> sum(path) > target
# Backtracking step -> pop the last number added

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if sum(path) == target:
                res.append(path[:])
                return
            
            if i == len(nums):
                return
            
            if sum(path) > target:
                return

            path.append(nums[i])
            backtrack(i, path)
            path.pop()
            backtrack(i + 1, path)
            
        
        backtrack(0, [])
        return res