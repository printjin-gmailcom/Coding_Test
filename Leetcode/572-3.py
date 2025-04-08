class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if isSameTree(node, subRoot):
                return True
            stack.append(node.left)
            stack.append(node.right)
    return False

def isSameTree(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
