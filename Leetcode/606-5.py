class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return ""
        
        result = []
        
        def preorder(node):
            if not node:
                return
            
            result.append(str(node.val))
            
            if node.left or node.right:
                result.append("(")
                preorder(node.left)
                result.append(")")
            
            if node.right:
                result.append("(")
                preorder(node.right)
                result.append(")")
        
        preorder(root)
        return "".join(result)
