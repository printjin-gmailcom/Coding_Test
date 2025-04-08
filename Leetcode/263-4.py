class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            n = (lambda n, factor: n // factor if n % factor == 0 else n)(n, factor)
        return n == 1
