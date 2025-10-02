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


class Solution:
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return ''.join(res[::-1])


class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


class Solution:
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0 
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


from typing import List

class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


from typing import List
class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1] 
            elif current_sum < target:
                left += 1
            else:
                right -= 1


from typing import List
class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count


from typing import List
class Solution:
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left = 0
        current_sum = 0
        min_len = float('inf')
        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len


from typing import List
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]


from typing import List
class Solution:
    def getRow(self, rowIndex):
        row = [1] + [0] * rowIndex
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row


class Solution:
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])


class Solution:
    def reverseWords(self, s):
        return ' '.join(word[::-1] for word in s.split(' '))


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


class Solution:
    def moveZeroes(self, nums):
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
