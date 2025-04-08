def validPalindrome(s: str) -> bool:
    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]
    
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i+1:]):
            return True
    
    return is_palindrome(s)
