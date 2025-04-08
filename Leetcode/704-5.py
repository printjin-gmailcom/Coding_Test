def search(nums: list[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1
