class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid2[x][y] == 0:
                return True
            grid2[x][y] = 0  # Mark the cell as visited
            is_sub_island = grid1[x][y] == 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                is_sub_island = dfs(x + dx, y + dy) and is_sub_island
            return is_sub_island
        
        m, n = len(grid2), len(grid2[0])
        sub_islands_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_islands_count += 1
        
        return sub_islands_count