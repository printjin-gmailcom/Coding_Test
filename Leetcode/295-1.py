import heapq

class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        
        if self.low and self.high and (-self.low[0] > self.high[0]):
            to_move = -heapq.heappop(self.low)
            heapq.heappush(self.high, to_move)
        
        if len(self.low) > len(self.high) + 1:
            to_move = -heapq.heappop(self.low)
            heapq.heappush(self.high, to_move)
        elif len(self.high) > len(self.low):
            to_move = heapq.heappop(self.high)
            heapq.heappush(self.low, -to_move)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0] + self.high[0]) / 2
