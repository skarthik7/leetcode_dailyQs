# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(root, value, path):
            if not root:
                return False
            if root.val == value:
                return True
            path.append('L')
            if findPath(root.left, value, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, value, path):
                return True
            path.pop()
            return False
        
        pathToStart, pathToDest = [], []
        findPath(root, startValue, pathToStart)
        findPath(root, destValue, pathToDest)
        
        i = 0
        while i < min(len(pathToStart), len(pathToDest)) and pathToStart[i] == pathToDest[i]:
            i += 1
        
        directions = 'U' * (len(pathToStart) - i)
        directions += ''.join(pathToDest[i:])
        
        return directions
        
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Space Complexity: O(H) where H is the height of the binary