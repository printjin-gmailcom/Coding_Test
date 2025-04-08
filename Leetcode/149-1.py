from typing import List
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1, p2):
            dy = p2[1] - p1[1]
            dx = p2[0] - p1[0]
            if dx == 0:
                return ('inf', 0)
            if dy == 0:
                return (0, 'inf')
            g = gcd(dy, dx)
            return (dy // g, dx // g)
        
        n = len(points)
        if n <= 1:
            return n
        
        max_points = 1
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1
            for j in range(i + 1, n):
                if points[i] == points[j]:
                    duplicate += 1
                else:
                    sl = slope(points[i], points[j])
                    slopes[sl] += 1
            max_points = max(max_points, duplicate + max(slopes.values(), default=0))
        
        return max_points
