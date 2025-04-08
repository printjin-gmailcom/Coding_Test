class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def postorder(node):
            if not node:
                return ""
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            if not left and not right:
                return str(node.val)
            if not right:
                return f"{node.val}({left})"
            return f"{node.val}({left})({right})"
        
        return postorder(root)
