def wordPattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    return [pattern.index(c) for c in pattern] == [words.index(word) for word in words]
