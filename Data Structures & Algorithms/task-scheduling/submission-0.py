# tasks
# identical tasks are separated by at least n (task[i] == next task)
# return min CPU cycles to complete

import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        least = 0
        maxHeap = []

        counter = {}
        for t in tasks:
            if t not in counter:
                counter[t] = -1
            else:
                counter[t] -= 1

        maxHeap = [(count, task) for (task, count) in counter.items()]
        heapq.heapify(maxHeap)
        queue = deque()

        while maxHeap or queue:
            if queue and queue[0][0] == least:
                heapq.heappush(maxHeap, (queue[0][1], queue[0][2]))
                queue.popleft()

            if maxHeap:
                if maxHeap[0][0] != -1:
                    queue.append((least + n + 1, maxHeap[0][0] + 1, maxHeap[0][1]))
                heapq.heappop(maxHeap)
            least += 1

        return least