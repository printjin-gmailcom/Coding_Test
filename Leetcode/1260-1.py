class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        flat_grid = [grid[i][j] for i in range(m) for j in range(n)]
        k = k % (m * n)
        
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        
        new_grid = [[flat_grid[i * n + j] for j in range(n)] for i in range(m)]
        return new_grid
