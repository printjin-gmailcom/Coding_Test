class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, i = 0, len(s) - 1
        
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
