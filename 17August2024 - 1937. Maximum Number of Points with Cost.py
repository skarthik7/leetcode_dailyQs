class Solution:
    def maxPoints(self, points: List[List[int]]) -> int: #dp
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for r in range(1, m):
            left = [0] * n
            right = [0] * n

            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, dp[c])

            right[n - 1] = dp[n - 1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, dp[c])

            for c in range(n):
                dp[c] = points[r][c] + max(left[c], right[c])

        return max(dp)