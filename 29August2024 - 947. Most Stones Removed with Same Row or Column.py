class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        for x, y in stones:
            if (x, 'row') not in parent:
                parent[(x, 'row')] = (x, 'row')
            if (y, 'col') not in parent:
                parent[(y, 'col')] = (y, 'col')
            union((x, 'row'), (y, 'col'))
        
        unique_roots = len({find(x) for x in parent})
        return len(stones) - unique_roots