import re

def isPalindrome(s):
    filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return filtered_s == filtered_s[::-1]
