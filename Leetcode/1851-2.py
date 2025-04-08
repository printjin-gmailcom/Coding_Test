import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        queries_with_index = sorted((q, i) for i, q in enumerate(queries))
        result = [-1] * len(queries)
        min_heap = []
        interval_index = 0
        
        for query, original_index in queries_with_index:
            while interval_index < len(intervals) and intervals[interval_index][0] <= query:
                start, end = intervals[interval_index]
                heapq.heappush(min_heap, (end - start + 1, end))
                interval_index += 1
            
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[original_index] = min_heap[0][0]
        
        return result
