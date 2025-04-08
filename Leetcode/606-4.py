from collections import deque

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        queue = deque([(root, False)])
        result = ""
        
        while queue:
            node, visited = queue.popleft()
            
            if visited:
                result += ")"
            else:
                result += f"({node.val}"
                queue.appendleft((node, True))
                
                if node.left is None and node.right:
                    result += "()"
                
                if node.right:
                    queue.appendleft((node.right, False))
                
                if node.left:
                    queue.appendleft((node.left, False))
        
        return result[1:-1]  
