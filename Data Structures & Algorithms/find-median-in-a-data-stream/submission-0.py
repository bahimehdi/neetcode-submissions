class MedianFinder:

    def __init__(self):
        self.maxHeap = list()
        self.minHeap = list()
        

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        while abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            if len(self.maxHeap) > len(self.minHeap):
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            else:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        elif len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2