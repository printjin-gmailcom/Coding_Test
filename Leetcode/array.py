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
    

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: return []
        m, n = len(mat), len(mat[0])
        res = []
        for s in range(m + n - 1):
            start_i = max(0, s - (n - 1))
            end_i = min(m - 1, s)
            if s % 2 == 0:
                i = end_i
                while i >= start_i:
                    j = s - i
                    res.append(mat[i][j])
                    i -= 1
            else:
                i = start_i
                while i <= end_i:
                    j = s - i
                    res.append(mat[i][j])
                    i += 1
        return res


class Solution:
    def spiralOrder(self, matrix):
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res


class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            row = [1]
            for j in range(1, len(prev)):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            res.append(row)
        return res
