class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        dp_prev = [0] * (k + 1)
        dp_curr = [0] * (k + 1)
        dp_prev[0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp_curr[j] = (dp_prev[j-1] * (i-1) + dp_prev[j] * (i-1)) % MOD
            dp_prev = dp_curr[:]
        
        return dp_prev[k]
