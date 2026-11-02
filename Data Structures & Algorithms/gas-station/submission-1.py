# Goal: return index i of gas[i] that can complete a full circle, else, return -1
# Choice: which station to start from
# Greedy: when accumulated fuel becomes negative, discard the current starting point, and take the next point as the best
# Safety: if sum(gas) < sum(cost) just avoids it

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        best = 0
        gasLeft = 0
        gasTotal = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            gasLeft += net
            gasTotal += net
            if gasLeft < 0:
                gasLeft = 0
                best = i + 1
        
        return best if gasTotal >= 0 else -1