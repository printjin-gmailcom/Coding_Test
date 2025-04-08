from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (1 << n)
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        max_performance = 0
        for i in range(1 << n):
            if bin(i).count('1') > k:
                continue
            min_eff = float('inf')
            speed_sum = 0
            for j in range(n):
                if i & (1 << j):
                    min_eff = min(min_eff, engineers[j][0])
                    speed_sum += engineers[j][1]
            if min_eff != float('inf'):
                max_performance = max(max_performance, speed_sum * min_eff)
        
        return max_performance % MOD
