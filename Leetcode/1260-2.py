class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        new_grid = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                new_pos = (i * n + j + k) % (m * n)
                new_i, new_j = divmod(new_pos, n)
                new_grid[new_i][new_j] = grid[i][j]
        
        return new_grid
