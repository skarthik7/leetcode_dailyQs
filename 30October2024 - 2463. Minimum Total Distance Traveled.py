class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        m, n = len(robot), len(factory)
        
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0

        # dp table        
        for j in range(1, n + 1):
            dp[0][j] = 0
            factory_position, factory_limit = factory[j - 1]
            
            for i in range(1, m + 1):
                dp[i][j] = dp[i][j - 1]
                
                total_distance = 0
                for k in range(1, min(factory_limit, i) + 1):
                    total_distance += abs(robot[i - k] - factory_position)
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_distance)
        return dp[m][n]