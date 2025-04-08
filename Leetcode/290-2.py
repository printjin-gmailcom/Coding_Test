def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    mapping = {}
    
    for c, word in zip(pattern, words):
        if c in mapping:
            if mapping[c] != word:
                return False
        elif word in mapping.values():
            return False
        else:
            mapping[c] = word
    
    return True
