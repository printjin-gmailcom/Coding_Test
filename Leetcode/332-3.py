from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        
        for src in graph:
            graph[src].sort(reverse=True)
        
        stack = ["JFK"]
        result = []
        
        while stack:
            node = stack[-1]
            if graph[node]:
                stack.append(graph[node].pop())
            else:
                result.append(stack.pop())
        
        return result[::-1]
