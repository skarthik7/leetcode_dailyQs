import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        maxHeap = []
        i = 0
        
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                # Push the profit into the max heap (invert the profit to use min heap as max heap)
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            
            if maxHeap:
                # Pop the project with the maximum profit
                w -= heapq.heappop(maxHeap)
            else:
                # No more projects can be afforded
                break
        
        return w