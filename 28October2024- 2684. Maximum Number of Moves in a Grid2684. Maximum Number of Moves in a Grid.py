class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        directions = [-1, 0, 1]

        def dfs(i, j, prev_val):
            if i < 0 or i >= m or j >= n or grid[i][j] <= prev_val:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = max(dfs(i+di, j+1, grid[i][j]) for di in directions) + 1
            return dp[i][j]

        return max(dfs(i, 0, -1) for i in range(m))-1

