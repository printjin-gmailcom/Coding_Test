import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        self.max_heap = [-n for n in nums]
        heapq.heapify(self.max_heap)
        while len(self.max_heap) > k:
            heapq.heappop(self.max_heap)
        for _ in range(min(k, len(nums))):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        return self.min_heap[0]
