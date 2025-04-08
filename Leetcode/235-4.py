class Solution:
    def findPath(self, root: TreeNode, path: list, k: int) -> bool:
        if not root:
            return False
        
        path.append(root)
        
        if root.val == k:
            return True
        
        if (root.left and self.findPath(root.left, path, k)) or (root.right and self.findPath(root.right, path, k)):
            return True
        
        path.pop()
        return False
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1, path2 = [], []
        
        if not self.findPath(root, path1, p.val) or not self.findPath(root, path2, q.val):
            return None
        
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1
        
        return path1[i-1]
