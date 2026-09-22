import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(x**2 + y**2, x, y) for (x, y) in points]
        heapq.heapify(points)
        closest = []
        for i in range(k):
            closest.append(heapq.heappop(points)[1:])
        return closest