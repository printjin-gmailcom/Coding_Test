from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        def contains_all(window_count, t_count):
            for char in t_count:
                if window_count[char] < t_count[char]:
                    return False
            return True
        
        t_count = Counter(t)
        min_len = float('inf')
        min_len_start = 0
        
        for i in range(len(s)):
            window_count = Counter()
            for j in range(i, len(s)):
                window_count[s[j]] += 1
                if contains_all(window_count, t_count):
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        min_len_start = i
                    break
        
        return s[min_len_start:min_len_start + min_len] if min_len != float('inf') else ""
