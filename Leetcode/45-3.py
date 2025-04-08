from typing import List
from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        jumps = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                if current == n - 1:
                    return jumps
                
                for i in range(1, nums[current] + 1):
                    next_index = current + i
                    if next_index < n and not visited[next_index]:
                        visited[next_index] = True
                        queue.append(next_index)
            
            jumps += 1
        
        return -1  # This line will never be reached due to problem constraints
