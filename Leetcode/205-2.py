def isIsomorphic(s, t):
    mapping = {}
    mapped = set()
    
    for char_s, char_t in zip(s, t):
        if char_s in mapping:
            if mapping[char_s] != char_t:
                return False
        else:
            if char_t in mapped:
                return False
            mapping[char_s] = char_t
            mapped.add(char_t)
    
    return True
