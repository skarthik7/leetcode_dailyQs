class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Check if the first node of the first edge is in the second edge
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]