def findDisappearedNumbers(nums: list[int]) -> list[int]:
    n = len(nums)
    count = [0] * n
    for num in nums:
        count[num - 1] += 1
    return [i + 1 for i in range(n) if count[i] == 0]
