class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        hFences.sort()
        hn = len(hFences)
        hset = set()
        for hi in range(hn - 1):
            for hj in range(hi + 1, hn):
                hset.add(hFences[hj] - hFences[hi])

        vFences.append(1)
        vFences.append(n)
        vFences.sort()
        vn = len(vFences)
        vset = set()
        for vi in range(vn - 1):
            for vj in range(vi + 1, vn):
                vset.add(vFences[vj] - vFences[vi])

        test = hset.intersection(vset)
        if not test:
            return -1
        modulo = 10**9 + 7
        max_sq = max(test)
        return max_sq ** 2 % modulo