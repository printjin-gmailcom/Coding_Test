from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.data = SortedList()

    def addNum(self, num: int) -> None:
        self.data.add(num)

    def findMedian(self) -> float:
        n = len(self.data)
        if n % 2 == 1:
            return float(self.data[n // 2])
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2.0
