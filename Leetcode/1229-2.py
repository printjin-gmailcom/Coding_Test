class Solution:
    def replaceElements(self, arr):
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            if not stack:
                stack.append(arr[i])
                arr[i] = -1
            else:
                stack.append(max(stack[-1], arr[i]))
                arr[i] = stack[-2]
        return arr

solution = Solution()
arr = [17, 18, 5, 4, 6, 1]
print(solution.replaceElements(arr))  # Output: [18, 6, 6, 6, 1, -1]
