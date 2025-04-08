from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            min_height = heights[i]
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        
        return max_area
