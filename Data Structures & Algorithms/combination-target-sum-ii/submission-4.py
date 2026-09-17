# The base case -> sum(path) == target
# Choices -> recurse with candidates[i], recurse with candidates[i+1]
# Constraints -> sum(path) > target and no dups
# Backtracking step -> pop the last number added

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if sum(path) == target:
                res.append(path[:])
                return

            if i == len(candidates) or sum(path) > target:
                return

            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            path.append(candidates[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(j, path)
            
        candidates.sort()
        backtrack(0, [])
        return res