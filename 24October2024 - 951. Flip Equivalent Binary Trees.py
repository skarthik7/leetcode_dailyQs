# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        
        without_flip = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        with_flip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        
        return without_flip or with_flip
    
# The time complexity of the flipEquiv function is O(n), where n is the total number of nodes in the larger of the two binary trees (root1 and root2).
# The space complexity is O(h), where h is the height of the tree. 