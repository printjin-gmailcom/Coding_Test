from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        window_count = Counter()
        
        required = len(t_count)
        formed = 0
        
        l, r = 0, 0
        min_len = float('inf')
        min_len_start = 0
        
        while r < len(s):
            char = s[r]
            window_count[char] += 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_len_start = l
                
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                l += 1
            
            r += 1
        
        return s[min_len_start:min_len_start + min_len] if min_len != float('inf') else ""
