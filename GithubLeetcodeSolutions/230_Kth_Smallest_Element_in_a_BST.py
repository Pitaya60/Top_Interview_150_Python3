class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            
            # Traverse the left subtree
            left_values = inorder(node.left) if node.left else []
            
            # Visit the current node
            current_value = [node.val]
            
            # Traverse the right subtree
            right_values = inorder(node.right) if node.right else []
            
            return left_values + current_value + right_values

        values = inorder(root)
        
        if 1 <= k <= len(values):
            return values[k - 1]
        else:
            return None
