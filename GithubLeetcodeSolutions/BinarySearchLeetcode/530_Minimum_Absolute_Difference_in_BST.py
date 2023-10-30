class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root) -> int:
        def in_order_traversal(node):
            nonlocal prev, min_diff
            if not node:
                return
            in_order_traversal(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            in_order_traversal(node.right)

        prev = None
        min_diff = float('inf')
        in_order_traversal(root)
        return min_diff

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
result = solution.getMinimumDifference(root)
print(result) 