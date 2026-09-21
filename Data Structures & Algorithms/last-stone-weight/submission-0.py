import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        x = y = 0
        while len(stones) > 2:
            x = stones[0]
            y = min(stones[1], stones[2])
            if stones[0] == y:
                heapq.heappop(stones)
                heapq.heappop(stones)
            else:
                heapq.heappop(stones)
                heapq.heappop(stones)
                heapq.heappush(stones, x - y)
        if len(stones) == 2:
            if stones[0] == stones[1]:
                return 0
            else:
                stones[0] = stones[0] - stones[1]
        return -stones[0]