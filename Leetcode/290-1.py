def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for c, word in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != word:
                return False
        else:
            if word in word_to_char:
                return False
            char_to_word[c] = word
            word_to_char[word] = c
    
    return True
