class Solution:
    def replaceElements(self, arr):
        max_right = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            if current > max_right:
                max_right = current
        return arr

solution = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(solution.replaceElements(arr))  # Output: [18, 6, 6, 6, 1, -1]
