class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        bought = prices[0] + prices[1]
        if money >= bought:
            return money - bought
        return money