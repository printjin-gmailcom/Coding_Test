class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        current = root
        while current:
            if current.left:
                pre = current.left
                while pre.right:
                    pre = pre.right
                pre.right = current.right
                current.left, current.right = None, current.left
            current = current.left if current.left else current.right
        return root

# 트리를 레벨 순서로 출력
def print_tree_level_order_morris(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

if __name__ == "__main__":
    # 트리 생성
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Before inversion (Level order):")
    print_tree_level_order_morris(root)
    
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("\nAfter inversion (Level order):")
    print_tree_level_order_morris(inverted_root)
