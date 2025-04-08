def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(map(lambda x: x * x, nums))
