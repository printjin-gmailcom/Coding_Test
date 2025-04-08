class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToString(root):
    if not root:
        return "X"
    return f"#{root.val} {treeToString(root.left)} {treeToString(root.right)}"

def isSubtree(root, subRoot):
    return treeToString(subRoot) in treeToString(root)
