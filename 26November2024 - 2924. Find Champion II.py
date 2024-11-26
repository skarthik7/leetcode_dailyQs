#https://leetcode.com/problems/find-champion-ii/
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n
        for _, v in edges:
            incoming[v] += 1
        
        champion = -1
        for i in range(n):
            if incoming[i] == 0:
                if champion != -1:
                    return -1
                champion = i
        
        return champion
# Time Complexity: O(N)