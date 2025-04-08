def isPalindrome(s):
    def checkPalindrome(l, r):
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if l >= r:
            return True
        if s[l].lower() != s[r].lower():
            return False
        return checkPalindrome(l + 1, r - 1)
    
    return checkPalindrome(0, len(s) - 1)
