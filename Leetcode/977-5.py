from collections import deque

def sortedSquares(nums: list[int]) -> list[int]:
    n = len(nums)
    left, right = 0, n - 1
    result = deque()

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.appendleft(nums[left] * nums[left])
            left += 1
        else:
            result.appendleft(nums[right] * nums[right])
            right -= 1

    return list(result)
