class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        max_profit = 0
        total_profit = 0
        j = 0
        
        for ability in worker:
            while j < len(jobs) and ability >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit