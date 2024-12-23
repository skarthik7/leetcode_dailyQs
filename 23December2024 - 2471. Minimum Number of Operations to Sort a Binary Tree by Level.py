# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def minSwaps(arr: List[int]) -> int:
            n = len(arr)
            arrpos = [(val, idx) for idx, val in enumerate(arr)]
            arrpos.sort()
            visited = [False] * n
            swaps = 0
            
            for i in range(n):
                if visited[i] or arrpos[i][1] == i:
                    continue
                
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = arrpos[j][1]
                    cycle_size += 1
                
                if cycle_size > 0:
                    swaps += (cycle_size - 1)
            
            return swaps
        
        queue = deque([root])
        total_swaps = 0
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            total_swaps += minSwaps(level_values)
        
        return total_swaps