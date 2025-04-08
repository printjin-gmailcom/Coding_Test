class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        result = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                new_j = (j + k) % n
                wrap_around = (j + k) // n
                new_i = (i + wrap_around) % m
                result[new_i][new_j] = grid[i][j]
        
        return result
