from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            stack = [(node, 0)]
            depth = {}
            while stack:
                node, d = stack.pop()
                if node:
                    depth[node] = d
                    stack.append((node.left, d + 1))
                    stack.append((node.right, d + 1))
            return depth

        depth_from_root = dfs(root)
        farthest_node = max(depth_from_root, key=depth_from_root.get)
        depth_from_farthest = dfs(farthest_node)
        return max(depth_from_farthest.values()) - 1
