def guessNumber(n: int) -> int:
    for num in range(1, n + 1):
        if guess(num) == 0:
            return num
