from collections import deque

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False
    queue = deque([(root, targetSum - root.val)])
    while queue:
        node, curr_sum = queue.popleft()
        if not node.left and not node.right and curr_sum == 0:
            return True
        if node.left:
            queue.append((node.left, curr_sum - node.left.val))
        if node.right:
            queue.append((node.right, curr_sum - node.right.val))
    return False
