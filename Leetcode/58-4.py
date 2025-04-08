class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        length = 0
        for char in s[::-1]:
            if char == ' ' and length > 0:
                break
            elif char != ' ':
                length += 1
        return length
