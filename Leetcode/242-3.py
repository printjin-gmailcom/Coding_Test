def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    for char in t:
        count[ord(char) - ord('a')] -= 1
    
    for c in count:
        if c != 0:
            return False
    
    return True

print(is_anagram("anagram", "nagaram"))  
print(is_anagram("rat", "car"))        
