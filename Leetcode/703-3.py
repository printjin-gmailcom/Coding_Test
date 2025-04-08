import bisect

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        return self.nums[-self.k]
