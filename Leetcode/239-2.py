from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        max_values = []
        
        for i in range(len(nums) - k + 1):
            max_values.append(max(nums[i:i+k]))
        
        return max_values
