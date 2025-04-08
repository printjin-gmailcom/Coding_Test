from collections import defaultdict, deque
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)
        
        for src in graph:
            graph[src].sort(reverse=True)
        
        result = []
        
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            result.append(node)
        
        dfs("JFK")
        return result[::-1]
