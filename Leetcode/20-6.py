class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in pair:
                stack.append(char)
            elif char in pair.values():
                if stack and pair[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return not stack
