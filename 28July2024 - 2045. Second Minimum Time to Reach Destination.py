# 2045. Second Minimum Time to Reach Destination


import heapq
from collections import defaultdict, deque

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        pq = [(0, 1, 0)]  # (current_time, current_vertex, visit_count)
        visited = defaultdict(lambda: [float('inf'), float('inf')])
        visited[1][0] = 0
        
        while pq:
            curr_time, u, visit_count = heapq.heappop(pq)
            if u == n and visit_count == 1:
                return curr_time
            
            if (curr_time // change) % 2 == 1:
                curr_time = (curr_time // change + 1) * change
            
            for v in graph[u]:
                next_time = curr_time + time
                
                if next_time < visited[v][0]:
                    visited[v][1] = visited[v][0]
                    visited[v][0] = next_time
                    heapq.heappush(pq, (next_time, v, 0))
                elif visited[v][0] < next_time < visited[v][1]:
                    visited[v][1] = next_time
                    heapq.heappush(pq, (next_time, v, 1))
        
        return -1


# Time Complexity: O(nlogn)