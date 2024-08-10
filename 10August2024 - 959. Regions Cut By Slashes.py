class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)
        
        for r in range(n):
            for c in range(n):
                index = 4 * (r * n + c)
                if grid[r][c] == '/':
                    uf.union(index, index + 3)
                    uf.union(index + 1, index + 2)
                elif grid[r][c] == '\\':
                    uf.union(index, index + 1)
                    uf.union(index + 2, index + 3)
                else:
                    uf.union(index, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)
                
                if r + 1 < n:
                    uf.union(index + 2, index + 4 * n)
                if c + 1 < n:
                    uf.union(index + 1, index + 7)
        
        return sum(uf.find(x) == x for x in range(4 * n * n))
