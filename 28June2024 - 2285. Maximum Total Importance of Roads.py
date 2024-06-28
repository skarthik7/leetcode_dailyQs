from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connections = defaultdict(int)
        for a, b in roads:
            connections[a] += 1
            connections[b] += 1
        
        sorted_cities = sorted(connections.items(), key=lambda x: x[1], reverse=True)
        
        importance = {}
        current_importance = n
        for city, _ in sorted_cities:
            importance[city] = current_importance
            current_importance -= 1
        
        for city in range(n):
            if city not in importance:
                importance[city] = current_importance
                current_importance -= 1
        
        total_importance = 0
        for a, b in roads:
            total_importance += importance[a] + importance[b]
        
        return total_importance

# Time complexity: O(nlogn)