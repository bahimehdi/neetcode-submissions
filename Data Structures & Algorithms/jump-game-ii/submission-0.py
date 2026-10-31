class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1

        if n == 0:
            return 0

        end = best = nums[0]
        count = 1

        if end >= n:
            return count

        for i in range(1, n+1):
            best = max(best, i + nums[i])

            if i == end:
                count += 1
                end = best

                if end >= n:
                    return count
                    
        return count