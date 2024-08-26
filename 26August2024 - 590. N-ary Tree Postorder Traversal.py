"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            output.append(node.val)
            for child in node.children:
                stack.append(child)
        
        return output[::-1]
# Time complexity: O(n)