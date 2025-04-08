def validPalindrome(s: str) -> bool:
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    
    while left < right:
        if s_list[left] != s_list[right]:
            return s_list[left:right] == s_list[left:right][::-1] or s_list[left+1:right+1] == s_list[left+1:right+1][::-1]
        left += 1
        right -= 1
    
    return True
