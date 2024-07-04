# 2192. All Ancestors of a Node in a Directed Acyclic Graph
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for edge in edges:
            from_node, to_node = edge
            graph[to_node].append(from_node) 
        answer = [[] for _ in range(n)]
        
        def dfs(v, ancestors):
            for ancestor in graph[v]:
                if ancestor not in ancestors:
                    ancestors.add(ancestor)
                    dfs(ancestor, ancestors)
        
        for i in range(n):
            ancestors = set()
            dfs(i, ancestors)
            answer[i] = sorted(list(ancestors))
        
        return answer
