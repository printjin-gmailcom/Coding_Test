from collections import deque

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        queue = deque([grid[i][j] for i in range(m) for j in range(n)])
        queue.rotate(k)
        
        new_grid = [[queue.popleft() for _ in range(n)] for _ in range(m)]
        return new_grid
