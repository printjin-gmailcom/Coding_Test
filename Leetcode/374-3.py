def guessNumber(n: int) -> int:
    def binary_search(left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == -1:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)
    
    return binary_search(1, n)
