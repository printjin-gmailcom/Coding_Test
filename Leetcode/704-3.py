import bisect

def search(nums: list[int], target: int) -> int:
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    return -1
