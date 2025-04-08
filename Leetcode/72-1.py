class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert_cost = 1 + dfs(i, j + 1) 
                delete_cost = 1 + dfs(i + 1, j)  
                replace_cost = 1 + dfs(i + 1, j + 1)  
                memo[(i, j)] = min(insert_cost, delete_cost, replace_cost)
            
            return memo[(i, j)]

        return dfs(0, 0)
