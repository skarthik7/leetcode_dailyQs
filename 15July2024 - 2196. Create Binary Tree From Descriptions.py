# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodeMap = {}
        childSet = set()
        for parent, child, _ in descriptions:
            if parent not in nodeMap:
                nodeMap[parent] = TreeNode(parent)
            if child not in nodeMap:
                nodeMap[child] = TreeNode(child)
            childSet.add(child)

        for parent, child, isLeft in descriptions:
            if isLeft:
                nodeMap[parent].left = nodeMap[child]
            else:
                nodeMap[parent].right = nodeMap[child]

        rootVal = (set(nodeMap.keys()) - childSet).pop()  # The root is not a child
        return nodeMap[rootVal]
# Time Complexity: O(N) where N is the number of nodes in the binary tree.