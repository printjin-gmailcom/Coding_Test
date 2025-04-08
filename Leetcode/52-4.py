class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(row, columns, diag1, diag2):
            if row == n:
                self.result += 1
                return
            for col in range(n):
                if not columns[col] and not diag1[row - col + n - 1] and not diag2[row + col]:
                    columns[col] = diag1[row - col + n - 1] = diag2[row + col] = True
                    solve(row + 1, columns, diag1, diag2)
                    columns[col] = diag1[row - col + n - 1] = diag2[row + col] = False
        
        self.result = 0
        columns = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        solve(0, columns, diag1, diag2)
        return self.result
