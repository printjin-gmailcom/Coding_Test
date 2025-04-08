def inorderTraversal(root: TreeNode) -> list[int]:
    def inorder(node):
        if node:
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)
    
    return list(inorder(root))
