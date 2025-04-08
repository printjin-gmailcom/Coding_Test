def isPalindrome(s):
    filtered_s = ''.join(c.lower() for c in s if c.isalnum())
    return filtered_s == filtered_s[::-1]
