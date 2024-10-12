class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1] + 1, -1))
        print(events)
        events.sort()
        print(events)

        max_groups = 0
        current_groups = 0
        
        for event in events:
            current_groups += event[1]
            max_groups = max(max_groups, current_groups)
        
        return max_groups