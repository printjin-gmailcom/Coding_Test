class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            stack.extend(filter(None, [node.left, node.right]))
        return root

# 트리의 모든 노드를 깊이 우선 순회로 출력 (Preorder)
def print_tree_dfs(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

if __name__ == "__main__":
    # 트리 생성
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Before inversion (DFS order):")
    print_tree_dfs(root)
    
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("\nAfter inversion (DFS order):")
    print_tree_dfs(inverted_root)
