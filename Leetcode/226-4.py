class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return root and TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))

# 중위 순회로 트리 출력 (Left -> Root -> Right)
def print_tree_inorder(root):
    if root is None:
        return
    print_tree_inorder(root.left)
    print(root.val, end=' ')
    print_tree_inorder(root.right)

if __name__ == "__main__":
    # 트리 생성
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Before inversion (Inorder):")
    print_tree_inorder(root)
    
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("\nAfter inversion (Inorder):")
    print_tree_inorder(inverted_root)
