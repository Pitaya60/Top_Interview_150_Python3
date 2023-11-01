class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root:Optional[TreeNode], k: int) -> int: 
        def inorder(node): 

            if not node:
                return

            inorder(node.left)

            left_values = inorder(node.left)
            left_values.append(node.val)
            right_values = inorder(node.right)
            
            return left_values + right_values

        values = inorder(root)
        
        if 1 <= k <= len(values):
            return values[k - 1]
        else:
            return None