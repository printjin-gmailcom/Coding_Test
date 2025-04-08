def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    p_to_w = [pattern.index(c) for c in pattern]
    w_to_p = [words.index(w) for w in words]
    
    return p_to_w == w_to_p
