def inorderTraversal(root: TreeNode) -> list[int]:
    result = []
    current = root
    
    while current:
        if current.left is None:
            result.append(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right
    
    return result
