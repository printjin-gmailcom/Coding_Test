from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        deq = deque()
        max_values = []
        
        for i in range(len(nums)):
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            deq.append(i)
            
            if i >= k - 1:
                max_values.append(nums[deq[0]])
        
        return max_values
