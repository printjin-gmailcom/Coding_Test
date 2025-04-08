from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def normalize(x, y):
            if x == 0:
                return (float('inf'), 0)
            if y == 0:
                return (0, 1)
            g = gcd(x, y)
            return (x // g, y // g)
        
        n = len(points)
        if n <= 1:
            return n
        
        max_points = 1
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1
            for j in range(n):
                if i != j:
                    dx = points[j][0] - points[i][0]
                    dy = points[j][1] - points[i][1]
                    if dx == 0 and dy == 0:
                        duplicate += 1
                    else:
                        slopes[normalize(dx, dy)] += 1
            max_points = max(max_points, duplicate + max(slopes.values(), default=0))
        
        return max_points
