from collections import Counter

def containsDuplicate(nums: list[int]) -> bool:
    return any(count > 1 for count in Counter(nums).values())
