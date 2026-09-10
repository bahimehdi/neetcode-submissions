# Sliding window
# dynamic

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = float('inf')
        for i in range(len(prices)):
            if minimum >= prices[i]:
                minimum = prices[i]
            while i < len(prices):
                profit = max(profit, prices[i] - minimum)
                i += 1
        return profit