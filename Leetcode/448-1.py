def findDisappearedNumbers(nums: list[int]) -> list[int]:
    return list(set(range(1, len(nums) + 1)) - set(nums))
