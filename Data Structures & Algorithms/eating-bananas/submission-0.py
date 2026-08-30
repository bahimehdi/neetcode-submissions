# - Input
# piles = array of int
# piles[i] = number of bananas in the ith pile
# h = number of hours to eat all the bananas
# - Output
# k = minimum integer such that you can eat all the bananas within `h` hours
# - Rules
# You may decide k = number of bananas u can eat per hour in a chosen pile
# - Constraints
# You can choose to eat piles[i] in a single hour if k >= piles[i]
# You cannot eat from another pile in the same hour
# - Brute force: Sort, test each number in the list in ascending order until you find the minimal k that consumes piles under h
# - Binary search:
# Sort
# Binary search the median
# for i in piles: totalHours += i // k; if totalHours <= h
# do an inside if (M < k) => k = M
# then outside, move to L = M - 1
# else (totalHours > h): don't append to the stack, R = M + 1


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        N = len(piles)
        k = float("inf")
        L, R = 1, max(piles)
        while L <= R:
            totalHours = 0
            M = (L + R) // 2
            for i in piles:
                totalHours += (i + M - 1) // M
            if totalHours <= h:
                if M <= k:
                    k = M
                    minHours = totalHours
                R = M - 1
            else:
                L = M + 1
        return k