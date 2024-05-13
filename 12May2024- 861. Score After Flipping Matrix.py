class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        for j in range(1, n):
            zero_count = sum(grid[i][j] == 0 for i in range(m))
            if zero_count > m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        score = sum(int(''.join(map(str, row)), 2) for row in grid)

        return score