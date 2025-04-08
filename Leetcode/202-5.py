class Solution:
    def isNonCyclical(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1
