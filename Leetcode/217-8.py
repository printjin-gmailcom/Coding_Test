import itertools

def containsDuplicate(nums: list[int]) -> bool:
    return any(a == b for a, b in itertools.combinations(nums, 2))
