from typing import List

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [float('-inf')] * (size + 1)
    
    def update(self, index, value):
        index += 1
        while index <= self.size:
            self.tree[index] = max(self.tree[index], value)
            index += index & -index
    
    def query(self, index):
        max_value = float('-inf')
        index += 1
        while index > 0:
            max_value = max(max_value, self.tree[index])
            index -= index & -index
        return max_value

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        fenwick_tree = FenwickTree(len(nums))
        max_values = []
        
        for i in range(k):
            fenwick_tree.update(i, nums[i])
        
        max_values.append(fenwick_tree.query(k - 1))
        
        for i in range(k, len(nums)):
            fenwick_tree.update(i, nums[i])
            max_values.append(fenwick_tree.query(i))
        
        return max_values
