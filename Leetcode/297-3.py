from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def postorder(node):
            if not node:
                return ["null"]
            return postorder(node.left) + postorder(node.right) + [str(node.val)]
        
        return ",".join(postorder(root))
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def build_tree(values):
            val = values.pop()
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.right = build_tree(values)
            node.left = build_tree(values)
            return node
        
        values = data.split(",")
        return build_tree(values)
