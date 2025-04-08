from collections import defaultdict

def containsDuplicate(nums: list[int]) -> bool:
    count = defaultdict(int)
    for num in nums:
        count[num] += 1
        if count[num] > 1:
            return True
    return False
