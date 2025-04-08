import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        n = len(queries)
        result = [-1] * n
        min_heap = []
        i = 0
        
        for query, idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                heapq.heappush(min_heap, (end - start + 1, end))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[idx] = min_heap[0][0]
        
        return result
