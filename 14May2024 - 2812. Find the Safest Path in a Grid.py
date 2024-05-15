from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dp = [[-1] * n for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        # Add all thieves to the queue and update the distance
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    dist[i][j] = 0

        # Perform a multi-source BFS from all thieves at the same time
        while queue:
            x, y, d = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and d + 1 < dist[nx][ny]:
                    dist[nx][ny] = d + 1
                    queue.append((nx, ny, d + 1))

        # Find the maximum safeness factor of all paths leading to cell (n - 1, n - 1)
        dp[0][0] = dist[0][0]
        queue = deque([(0, 0)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] < min(dp[x][y], dist[nx][ny]):
                    dp[nx][ny] = min(dp[x][y], dist[nx][ny])
                    queue.append((nx, ny))

        return dp[n - 1][n - 1]