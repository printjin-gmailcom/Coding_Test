class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        try:
            reversed_x = int(str(x)[::-1])
            if reversed_x >= 2**31:
                return 0
            return sign * reversed_x
        except:
            return 0
