class Solution:
    def replaceElements(self, arr):
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr

solution = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(solution.replaceElements(arr))  # Output: [18, 6, 6, 6, 1, -1]
