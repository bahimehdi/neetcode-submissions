# Goal: return index i of gas[i] that can complete a full circle, else, return -1
# Choice: which station to start from
# Greedy: If gasLeft < 0, discard the current candidate and restart from i + 1.
# Safety: Failed segments allow eliminating their starting candidates; gasTotal >= 0 guarantees a valid start exists.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        best = 0
        gasLeft = 0
        totalGas = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            gasLeft += net
            totalGas += net
            if gasLeft < 0:
                gasLeft = 0
                best = i + 1
        
        return best if totalGas >= 0 else -1