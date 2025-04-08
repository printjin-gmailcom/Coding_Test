from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            if not node:
                return 0
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            return max(left_height, right_height) + 1
        
        self.max_diameter = 0
        getHeight(root)
        return self.max_diameter
