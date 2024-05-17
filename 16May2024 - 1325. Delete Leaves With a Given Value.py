# 1325. Delete Leaves With a Given Value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def removeLeaves(node):
            if node is None:
                return None
            node.left = removeLeaves(node.left)
            node.right = removeLeaves(node.right)
            if node.left is None and node.right is None and node.val == target:
                return None
            return node

        return removeLeaves(root)