class Solution:
    def replaceElements(self, arr):
        return [max(arr[i+1:]) for i in range(len(arr) - 1)] + [-1]

solution = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(solution.replaceElements(arr))  # Output: [18, 6, 6, 6, 1, -1]
