def guessNumber(n: int) -> int:
    left, right = 1, n
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        res1 = guess(mid1)
        res2 = guess(mid2)
        
        if res1 == 0:
            return mid1
        if res2 == 0:
            return mid2
        if res1 == -1:
            right = mid1 - 1
        elif res2 == 1:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1
