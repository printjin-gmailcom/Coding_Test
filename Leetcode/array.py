class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num
        return -1


class Solution:
    def dominantIndex(self, nums):
        max_val = max(nums)
        max_index = nums.index(max_val)
        second_max = max([x for x in nums if x != max_val], default=-1)
        if max_val >= 2 * second_max:
            return max_index
        return -1


class Solution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits