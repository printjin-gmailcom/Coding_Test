import random

def guessNumber(n: int) -> int:
    left, right = 1, n
    while left <= right:
        num = random.randint(left, right)
        result = guess(num)
        if result == 0:
            return num
        elif result == -1:
            right = num - 1
        else:
            left = num + 1
