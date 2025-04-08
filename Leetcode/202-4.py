class Solution:
    def isNonCyclical(self, n: int) -> bool:
        history = {}
        while n != 1:
            if n in history:
                return False
            history[n] = True
            n = sum(int(digit) ** 2 for digit in str(n))
        return True
