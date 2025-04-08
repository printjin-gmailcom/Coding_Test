class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        digits = []
        while x:
            digits.append(x % 10)
            x //= 10
        reversed_x = 0
        for digit in digits:
            reversed_x = reversed_x * 10 + digit
            if reversed_x > 2**31 - 1:
                return 0
        return sign * reversed_x
