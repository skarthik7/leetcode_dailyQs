class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        minutes = [convert_to_minutes(time) for time in timePoints]
        
        minutes.sort()
        
        min_diff = float('inf')
        n = len(minutes)
        
        for i in range(n):
            diff = (minutes[(i + 1) % n] - minutes[i]) % (24 * 60)
            min_diff = min(min_diff, diff)
        
        circular_diff = (minutes[0] + 24 * 60 - minutes[-1]) % (24 * 60)
        min_diff = min(min_diff, circular_diff)
        
        return min_diff