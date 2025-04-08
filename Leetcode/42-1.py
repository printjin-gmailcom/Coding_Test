from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        total_water = 0
        
        for i in range(1, n - 1):
            max_left = max(height[:i])
            max_right = max(height[i+1:])
            water = min(max_left, max_right) - height[i]
            if water > 0:
                total_water += water
        
        return total_water
