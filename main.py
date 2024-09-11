# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check_height(node):
            if not node:
                return 0, True  # height, is_balanced
            
            left_height, left_balanced = check_height(node.left)
            right_height, right_balanced = check_height(node.right)
            
            current_balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )
            
            current_height = 1 + max(left_height, right_height)
            
            return current_height, current_balanced
        
        _, balanced = check_height(root)
        return balanced
