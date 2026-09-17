# The base case -> i == len(nums)
# Choices -> recurse on used, undo used and recurse
# Constraints -> no dups
# Backtracking step -> pop the last number added

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(used, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                backtrack(used, path)
                path.pop()
                used.remove(i)

        backtrack(set(), [])
        return res