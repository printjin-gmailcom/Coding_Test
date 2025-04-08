class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def dfs(i: int, j: int) -> int:
            if i == m:
                return n - j
            if j == n:
                return m - i
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = dfs(i + 1, j + 1)
            else:
                insert_cost = 1 + dfs(i, j + 1)  # Insert
                delete_cost = 1 + dfs(i + 1, j)  # Delete
                replace_cost = 1 + dfs(i + 1, j + 1)  # Replace
                dp[i][j] = min(insert_cost, delete_cost, replace_cost)
            
            return dp[i][j]

        return dfs(0, 0)
