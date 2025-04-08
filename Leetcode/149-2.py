from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def get_slope(p1, p2):
            dy = p2[1] - p1[1]
            dx = p2[0] - p1[0]
            if dx == 0:
                return float('inf')
            return dy / dx
        
        n = len(points)
        if n <= 1:
            return n
        
        max_points = 1
        for i in range(n):
            slopes = defaultdict(int)
            for j in range(n):
                if i != j:
                    slopes[get_slope(points[i], points[j])] += 1
            max_points = max(max_points, max(slopes.values(), default=0) + 1)
        
        return max_points
