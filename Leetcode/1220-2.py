class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        prev = [1] * 5  

        for _ in range(1, n):
            curr = [0] * 5
            curr[0] = prev[1]  
            curr[1] = (prev[0] + prev[2]) % MOD 
            curr[2] = (prev[0] + prev[1] + prev[3] + prev[4]) % MOD  
            curr[3] = (prev[2] + prev[4]) % MOD 
            curr[4] = prev[0]  
            prev = curr
        
        return sum(prev) % MOD
