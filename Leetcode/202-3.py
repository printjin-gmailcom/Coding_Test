class Solution:
    def get_next(self, n: int) -> int:
        return sum(int(digit) ** 2 for digit in str(n))
    
    def isNonCyclical(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)
        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))
        return fast == 1
