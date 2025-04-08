from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        
        while result and result[-1] == "null":
            result.pop()
        
        return "[" + ",".join(result) + "]"
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None
        
        values = collections.deque(data[1:-1].split(","))
        root = TreeNode(int(values.popleft()))
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                left_val = values.popleft()
                if left_val != "null":
                    node.left = TreeNode(int(left_val))
                    queue.append(node.left)
                right_val = values.popleft()
                if right_val != "null":
                    node.right = TreeNode(int(right_val))
                    queue.append(node.right)
        
        return root
