def isPalindrome(s):
    stack = []
    filtered_s = ''.join(c.lower() for c in s if c.isalnum())
    
    for c in filtered_s:
        stack.append(c)
    
    for c in filtered_s:
        if c != stack.pop():
            return False
            
    return True
