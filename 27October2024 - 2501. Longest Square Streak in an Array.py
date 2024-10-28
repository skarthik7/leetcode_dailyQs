class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        streak_lengths = {}
        max_streak = -1

        def compute_streak(num):
            if num not in nums_set:
                return 0
            if num in streak_lengths:
                return streak_lengths[num]
            
            next_num = num * num
            streak = 1 + compute_streak(next_num)
            streak_lengths[num] = streak
            return streak

        for num in nums_set:
            streak = compute_streak(num)
            if streak >= 2:
                max_streak = max(max_streak, streak)

        return max_streak