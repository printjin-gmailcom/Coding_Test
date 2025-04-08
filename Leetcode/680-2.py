def validPalindrome(s: str) -> bool:
    def helper(i, j, deleted):
        if i >= j:
            return True
        if s[i] == s[j]:
            return helper(i + 1, j - 1, deleted)
        elif not deleted:
            return helper(i + 1, j, True) or helper(i, j - 1, True)
        else:
            return False
    
    return helper(0, len(s) - 1, False)
