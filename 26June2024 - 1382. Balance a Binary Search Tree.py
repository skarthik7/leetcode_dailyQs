# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_nodes = []
        
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            sorted_nodes.append(node)
            in_order_traversal(node.right)
        
        def build_balanced_bst(nodes):
            if not nodes:
                return None
            mid = len(nodes) // 2
            root = nodes[mid]
            root.left = build_balanced_bst(nodes[:mid])
            root.right = build_balanced_bst(nodes[mid+1:])
            return root
        
        in_order_traversal(root)
        return build_balanced_bst(sorted_nodes)