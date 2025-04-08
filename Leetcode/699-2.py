class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        from collections import Counter, defaultdict
        import itertools
        
        target_count = Counter(target)
        target_chars = ''.join(sorted(target_count))
        target_len = len(target_chars)
        
        sticker_counts = [Counter(sticker) for sticker in stickers]
        
        dp = {}
        
        def get_mask(s):
            return sum(1 << i for i, c in enumerate(target_chars) if c in s)
        
        def solve(mask):
            if mask == 0:
                return 0
            if mask in dp:
                return dp[mask]
            
            min_stickers = float('inf')
            for sticker in sticker_counts:
                new_mask = mask
                for i, char in enumerate(target_chars):
                    if sticker[char] > 0:
                        new_mask &= ~(1 << i) * min(sticker[char], (mask >> i) & 1)
                
                if new_mask != mask:
                    min_stickers = min(min_stickers, 1 + solve(new_mask))
            
            dp[mask] = min_stickers if min_stickers != float('inf') else -1
            return dp[mask]
        
        full_mask = (1 << target_len) - 1
        result = solve(full_mask)
        
        return result
