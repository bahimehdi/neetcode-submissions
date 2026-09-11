# Sliding window
# dynamic

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = float('inf')
        for i in prices:
            minimum = min(minimum, i)
            profit = max(profit, i - minimum)
        return profit