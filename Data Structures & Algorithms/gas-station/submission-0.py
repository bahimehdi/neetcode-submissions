# Goal: return index i of gas[i] that can complete a full circle, else, return -1
# Choice: which station to start from
# Greedy: ..
# Safety: if sum(gas) < sum(cost) just avoids it

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        best = 0
        gasLeft = 0

        for i in range(len(gas)):
            gasLeft += gas[i] - cost[i]
            if gasLeft < 0:
                gasLeft = 0
                best = i + 1
        
        return best
