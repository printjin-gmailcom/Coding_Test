def guessNumber(n: int) -> int:
    left, right = 1, n
    
    while left <= right:
        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right
        left += 1
        right -= 1
