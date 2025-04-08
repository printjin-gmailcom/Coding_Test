class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = 5 ** 0.5
        fib_n = (((1 + sqrt5) / 2) ** (n + 1) - ((1 - sqrt5) / 2) ** (n + 1)) / sqrt5
        return int(fib_n)
