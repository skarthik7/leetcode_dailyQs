# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Dictionary to store the height of each node
        height = {}
        # Dictionary to store the depth of each node
        depth = {}
        # Dictionary to store the maximum heights from each depth level
        max_heights_at_depth = defaultdict(list)
        
        # Calculate depth and height of each node using DFS
        def dfs(node, d):
            if not node:
                return -1
            depth[node.val] = d
            left_height = dfs(node.left, d + 1)
            right_height = dfs(node.right, d + 1)
            node_height = max(left_height, right_height) + 1
            height[node.val] = node_height
            max_heights_at_depth[d].append(node_height)
            return node_height
        
        # Initial DFS from the root to fill depth and height info
        dfs(root, 0)
        
        # Preprocess max_heights_at_depth to store only the top two heights per depth
        for d in max_heights_at_depth:
            max_heights_at_depth[d].sort(reverse=True)
        
        # Process each query to calculate the height of the tree after removal
        result = []
        for query in queries:
            # Node's depth and height
            d = depth[query]
            h = height[query]
            
            # Check the highest height after removing the subtree rooted at query
            if len(max_heights_at_depth[d]) == 1:
                # If there's only one height, removing it will mean height at this depth is -1
                new_tree_height = depth[root.val] + max((max_heights_at_depth[dd][0] if max_heights_at_depth[dd] else -1)
                                                        for dd in max_heights_at_depth)
            else:
                # Otherwise, use the second-highest height in this depth level
                if max_heights_at_depth[d][0] == h:
                    new_height = max_heights_at_depth[d][1]
                else:
                    new_height = max_heights_at_depth[d][0]
                # Compute the new height with the altered height at this level
                new_tree_height = max(depth[root.val], depth[root.val] + new_height)
                
            result.append(new_tree_height)
        
        return result