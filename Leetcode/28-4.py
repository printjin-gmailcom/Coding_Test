def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    
    lps = [0] * len(needle)
    j = 0
    
    for i in range(1, len(needle)):
        if needle[i] == needle[j]:
            j += 1
            lps[i] = j
        else:
            if j != 0:
                j = lps[j - 1]
                i -= 1
            else:
                lps[i] = 0
    
    i = 0
    j = 0
    
    while i < len(haystack):
        if needle[j] == haystack[i]:
            i += 1
            j += 1
            
        if j == len(needle):
            return i - j
        
        elif i < len(haystack) and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return -1
