from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        for c in ransom_count:
            if ransom_count[c] > magazine_count[c]:
                return False
        return True
