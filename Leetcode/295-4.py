from collections import defaultdict

class MedianFinder:

    def __init__(self):
        self.counts = defaultdict(int)
        self.total = 0

    def addNum(self, num: int) -> None:
        self.counts[num] += 1
        self.total += 1

    def findMedian(self) -> float:
        count = 0
        median1 = median2 = None
        for num in sorted(self.counts):
            count += self.counts[num]
            if median1 is None and count >= (self.total + 1) // 2:
                median1 = num
            if median2 is None and count >= (self.total + 2) // 2:
                median2 = num
                break
        return (median1 + median2) / 2.0 if median2 is not None else float(median1)
