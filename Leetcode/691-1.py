class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        from collections import Counter, defaultdict
        import functools
        
        target_count = Counter(target)
        target_len = len(target)
        
        sticker_counts = [Counter(sticker) for sticker in stickers]
        
        dp = {}
        
        @functools.lru_cache(None)
        def dfs(mask):
            if mask == 0:
                return 0
            if mask in dp:
                return dp[mask]
            
            min_stickers = float('inf')
            target_chars = [target[i] for i in range(target_len) if mask & (1 << i)]
            target_counter = Counter(target_chars)
            
            for sticker in sticker_counts:
                new_mask = mask
                for char, count in target_counter.items():
                    if sticker[char] > 0:
                        new_mask &= ~(1 << target.index(char)) * min(count, sticker[char])
                
                if new_mask != mask:
                    min_stickers = min(min_stickers, 1 + dfs(new_mask))
            
            dp[mask] = min_stickers if min_stickers != float('inf') else -1
            return dp[mask]
        
        full_mask = (1 << target_len) - 1
        result = dfs(full_mask)
