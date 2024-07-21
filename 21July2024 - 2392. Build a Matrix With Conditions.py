from typing import List
from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologicalSort(edges: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            in_degree = {i: 0 for i in range(1, k + 1)}
            for u, v in edges:
                graph[u].append(v)
                in_degree[v] += 1
            
            queue = deque([node for node in in_degree if in_degree[node] == 0])
            sorted_order = []
            while queue:
                node = queue.popleft()
                sorted_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            return sorted_order if len(sorted_order) == k else []
        
        row_order = topologicalSort(rowConditions)
        col_order = topologicalSort(colConditions)
        
        if not row_order or not col_order:
            return []
        
        matrix = [[0] * k for _ in range(k)]
        position = {num: i for i, num in enumerate(col_order)}
        
        for i, num in enumerate(row_order):
            matrix[i][position[num]] = num
        
        return matrix