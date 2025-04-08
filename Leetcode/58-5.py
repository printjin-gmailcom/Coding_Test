class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().splitlines()[-1].split()[-1])
