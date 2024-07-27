from typing import List, Dict, Tuple
import sys
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        transformation_map: Dict[str, List[Tuple[str, int]]] = {}
        for o, c, z in zip(original, changed, cost):
            if o not in transformation_map:
                transformation_map[o] = []
            transformation_map[o].append((c, z))
        
        def dijkstra(start: str, end: str) -> int:
            if start == end:
                return 0
            min_heap = [(0, start)]
            visited = set()
            while min_heap:
                current_cost, current_char = heapq.heappop(min_heap)
                if current_char in visited:
                    continue
                visited.add(current_char)
                if current_char == end:
                    return current_cost
                if current_char in transformation_map:
                    for next_char, trans_cost in transformation_map[current_char]:
                        if next_char not in visited:
                            heapq.heappush(min_heap, (current_cost + trans_cost, next_char))
            return sys.maxsize
        
        total_cost = 0
        for s_char, t_char in zip(source, target):
            cost = dijkstra(s_char, t_char)
            if cost == sys.maxsize:
                return -1
            total_cost += cost
        
        return total_cost
        
# Time complexity: O(n^2 * logn) because of dijkstra