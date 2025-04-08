from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        queue = deque([root])
        
        while queue:
            current = queue.popleft()
            # 자식 교환
            current.left, current.right = current.right, current.left
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
                
        return root

# 레벨 순서로 트리 출력 (BFS 순서)
def print_tree_level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.val, end=' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

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
    print_tree_level_order(root)
    
    solution = Solution()
    inverted_root = solution.invertTree(root)

    print("\nAfter inversion (Level order):")
    print_tree_level_order(inverted_root)
