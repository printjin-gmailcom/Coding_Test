def findDisappearedNumbers(nums: list[int]) -> list[int]:
    total = sum(range(1, len(nums) + 1))
    return [i for i in range(1, len(nums) + 1) if i not in nums]
