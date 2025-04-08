from collections import Counter

def majorityElement(nums: list[int]) -> int:
    count = Counter(nums)
    return max(count.keys(), key=count.get)
