class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0]*(n-2) for _ in range(n-2)]

        for i in range(1, n-1):
            for j in range(1, n-1):
                maxLocal[i-1][j-1] = max(max(grid[i-1:i+2][k][j-1:j+2]) for k in range(3))

        return maxLocal