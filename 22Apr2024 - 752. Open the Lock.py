class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        if '0000' in dead:
            return -1

        q = deque([('0000', 0)])
        visited = {'0000'}

        while q:
            node, dist = q.popleft()
            if node == target:
                return dist
            for nei in neighbors(node):
                if nei not in visited and nei not in dead:
                    visited.add(nei)
                    q.append((nei, dist+1))

        return -1
