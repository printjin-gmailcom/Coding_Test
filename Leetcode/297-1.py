from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(node):
            if not node:
                return ["null"]
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ",".join(preorder(root))
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def build_tree(nodes):
            val = next(nodes)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build_tree(nodes)
            node.right = build_tree(nodes)
            return node
        
        node_list = iter(data.split(","))
        return build_tree(node_list)
