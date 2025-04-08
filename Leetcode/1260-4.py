class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        
        for _ in range(k):
            previous = grid[-1][-1]
            for i in range(m):
                for j in range(n):
                    current = grid[i][j]
                    grid[i][j] = previous
                    previous = current
        
        return grid
