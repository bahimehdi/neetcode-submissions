# - input:
# weights: contains packages weights
# days: days to load the weights
# - output:
# capacity: minimum capacity to load the all `weights[i]` in `days`
# - binary search:
# L = lowest capacity = max(weights)
# R = highest capacity = sum(weights)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L, R = max(weights), sum(weights)
        while L < R:
            M = (L + R) // 2
            usedDays, currentLoad = 1, 0
            for i in weights:
                if currentLoad + i <= M:
                    currentLoad += i
                else:
                    currentLoad = i
                    usedDays += 1
            if usedDays > days:
                L = M + 1
            else:
                R = M
        return L