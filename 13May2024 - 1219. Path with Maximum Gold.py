class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            gold = grid[i][j]
            grid[i][j] = 0  # mark as visited
            max_gold = max(dfs(i-1, j), dfs(i+1, j), dfs(i, j-1), dfs(i, j+1))
            grid[i][j] = gold  # backtrack
            return gold + max_gold

        m, n = len(grid), len(grid[0])
        max_gold = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold