from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            if isSameTree(node, subRoot):
                return True
            queue.append(node.left)
            queue.append(node.right)
    return False

def isSameTree(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
