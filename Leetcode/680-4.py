def validPalindrome(s: str) -> bool:
    stack = [(0, len(s) - 1, False)]
    
    while stack:
        i, j, deleted = stack.pop()
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        if not deleted:
            stack.append((i + 1, j, True))
            stack.append((i, j - 1, True))
    
    return False
