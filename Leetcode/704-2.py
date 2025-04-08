def search(nums: list[int], target: int) -> int:
    def binary_search(left, right):
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid - 1)
    
    return binary_search(0, len(nums) - 1)
