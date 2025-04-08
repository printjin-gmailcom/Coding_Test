class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if (cols & (1 << col)) == 0 and (diag1 & (1 << (row - col + n - 1))) == 0 and (diag2 & (1 << (row + col))) == 0:
                    backtrack(row + 1, cols | (1 << col), diag1 | (1 << (row - col + n - 1)), diag2 | (1 << (row + col)))
        
        self.count = 0
        backtrack(0, 0, 0, 0)
        return self.count
