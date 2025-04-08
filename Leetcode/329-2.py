from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]
        
        def dfs(r, c):
            if memo[r][c] != -1:
                return memo[r][c]
            
            length = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    length = max(length, 1 + dfs(nr, nc))
            
            memo[r][c] = length
            return length
        
        return max(dfs(r, c) for r in range(rows) for c in range(cols))
