class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Step 1: Build the graph
        graph = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Step 2: Initialize the max-heap and probabilities
        max_heap = [(-1.0, start_node)]  # Use negative probabilities for max-heap
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0
        
        # Step 3: Dijkstra's algorithm to find the maximum probability path
        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob  # Convert back to positive
            
            if node == end_node:
                return current_prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = current_prob * edge_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0