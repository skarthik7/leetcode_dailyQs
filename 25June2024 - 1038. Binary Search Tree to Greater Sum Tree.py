# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        running_sum = 0
        
        def reverse_in_order(node):
            nonlocal running_sum
            if not node:
                return
            
            reverse_in_order(node.right)
            

            node.val += running_sum
            running_sum = node.val
            

            reverse_in_order(node.left)
        
        reverse_in_order(root)
        return root