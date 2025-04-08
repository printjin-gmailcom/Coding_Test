from typing import List

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)
    
    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
    
    def query(self, left, right):
        left += self.n
        right += self.n
        max_value = float('-inf')
        while left <= right:
            if left % 2 == 1:
                max_value = max(max_value, self.tree[left])
                left += 1
            if right % 2 == 0:
                max_value = max(max_value, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return max_value

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        segment_tree = SegmentTree(nums)
        max_values = []
        
        for i in range(len(nums) - k + 1):
            max_values.append(segment_tree.query(i, i + k - 1))
        
        return max_values
