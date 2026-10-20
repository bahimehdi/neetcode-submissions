class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = float('inf')
        for choco in prices:
            if choco < min1:
                min1, min2 = choco, min1
            elif choco < min2:
                min2 = choco
        
        bought = money - min1 - min2
        if bought >= 0:
            return bought
        return money