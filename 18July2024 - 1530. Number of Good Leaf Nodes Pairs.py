# 1530. Number of Good Leaf Nodes Pairs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.good_pairs = 0

        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            if not node.left and not node.right:
                leaf_depths = [0] * (distance + 1)
                leaf_depths[1] = 1
                return leaf_depths
            
            left_depths = dfs(node.left)
            right_depths = dfs(node.right)
            
            # Count good pairs
            for d1 in range(1, distance):
                for d2 in range(1, distance - d1 + 1):
                    self.good_pairs += left_depths[d1] * right_depths[d2]
            
            # Update depths for the current node
            new_depths = [0] * (distance + 1)
            for d in range(1, distance):
                new_depths[d + 1] = left_depths[d] + right_depths[d]
            
            return new_depths
        
        dfs(root)
        return self.good_pairs