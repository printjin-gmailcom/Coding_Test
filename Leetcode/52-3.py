class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(row, columns, diag1, diag2):
            if row == n:
                self.result += 1
                return
            for col in range(n):
                if col not in columns and (row - col) not in diag1 and (row + col) not in diag2:
                    solve(row + 1, columns | {col}, diag1 | {row - col}, diag2 | {row + col})
        
        self.result = 0
        solve(0, set(), set(), set())
        return self.result
