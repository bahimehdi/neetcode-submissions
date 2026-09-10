# Sliding window
# dynamic

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = j = 0
        minimum = float('inf')
        for i in range(len(prices)):
            if minimum >= prices[i]:
                j = i
                minimum = prices[i]
            while j < len(prices):
                profit = max(profit, prices[j] - minimum)
                j += 1
        return profit