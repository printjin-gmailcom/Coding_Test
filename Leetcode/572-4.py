class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root, subRoot):
    def dfs(node):
        if not node:
            return False
        if isSameTree(node, subRoot):
            return True
        return dfs(node.left) or dfs(node.right)

    def isSameTree(s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

    return dfs(root)
