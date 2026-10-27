class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if self.max_heap and num <= self.max_heap[0]:
            heapq.heappush_max(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))        

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0] / 1
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] / 1
        else:
            return (self.min_heap[0] + self.max_heap[0]) / 2
        
        