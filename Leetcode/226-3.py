class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        stack = [root]
        
        while stack:
            current = stack.pop()
            # 자식 교환
            current.left, current.right = current.right, current.left
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
                
        return root

# 후위 순회로 트리 출력 (Left -> Right -> Root)
def print_tree_postorder(root):
    if root is None:
        return
    print_tree_postorder(root.left)
    print_tree_postorder(root.right)
    print(root.val, end=' ')

if __name__ == "__main__":
    # 트리 생성
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Before inversion (Postorder):")
    print_tree_postorder(root)
    
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("\nAfter inversion (Postorder):")
    print_tree_postorder(inverted_root)
