def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(x * x for x in nums)
