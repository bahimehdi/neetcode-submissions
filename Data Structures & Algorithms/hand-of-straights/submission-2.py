from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand or groupSize == 1:
            return True
        
        if len(hand) % groupSize != 0:
            return False
        
        count = dict(sorted(Counter(hand).items()))

        for value in count:
            while count[value] > 0:
                count[value] -= 1
                for i in range(1, groupSize):
                    if value + i not in count or count[value + i] == 0:
                        return False
                    count[value + i] -= 1
                    
        return True