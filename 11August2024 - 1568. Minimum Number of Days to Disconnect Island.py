# 1568. Minimum Number of Days to Disconnect Island
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def is_connected(grid: List[List[int]]) -> bool:
            m, n = len(grid), len(grid[0])
            visited = [[False] * n for _ in range(m)]
            
            def dfs(x: int, y: int):
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
            found_island = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        if found_island:
                            return False  # More than one island found
                        dfs(i, j)
                        found_island = True
            # Check if all land cells are visited
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        return False
            return True
        def count_islands(grid: List[List[int]]) -> int:
            m, n = len(grid), len(grid[0])
            visited = [[False] * n for _ in range(m)]
            island_count = 0
            
            def dfs(x: int, y: int):
                if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0 or visited[x][y]:
                    return
                visited[x][y] = True
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and not visited[i][j]:
                        dfs(i, j)
                        island_count += 1
            
            return island_count
        if count_islands(grid) != 1:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Try removing one cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands(grid) != 1:
                        return 1
                    grid[i][j] = 1
        
        # Try removing two cells
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    for x in range(m):
                        for y in range(n):
                            if grid[x][y] == 1:
                                grid[x][y] = 0
                                if count_islands(grid) != 1:
                                    return 2
                                grid[x][y] = 1
                    grid[i][j] = 1
        
        return 2