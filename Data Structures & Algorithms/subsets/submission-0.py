# All backtracking problems can be broken down into the same 4 components:
# The base case -> i == len(nums)
# Choices -> add nums[i], don't add nums[i]
# Constraints -> none, since all nums are unique
# Backtracking step -> pop the last number added


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            
            # decision 1
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            # decision 2
            backtrack(i + 1, path)

        backtrack(0, [])
        return res