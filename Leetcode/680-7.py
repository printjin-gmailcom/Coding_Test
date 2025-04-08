def validPalindrome(s: str) -> bool:
    def check_palindrome_with_skip(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return check_palindrome_with_skip(left + 1, right) or check_palindrome_with_skip(left, right - 1)
        left += 1
        right -= 1
    
    return True
