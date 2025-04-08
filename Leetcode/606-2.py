class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        stack = [root]
        result = ""
        visited = set()
        
        while stack:
            node = stack[-1]
            
            if node in visited:
                stack.pop()
                result += ")"
            else:
                visited.add(node)
                result += f"({node.val}"
                
                if node.left is None and node.right:
                    result += "()"
                
                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)
        
        return result[1:-1]  # 처음과 끝의 괄호를 제거하여 반환
