from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffix_sums = [0] * n
        suffix_sums[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
        
        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix_sums[i]
            
            max_stones = 0
            for x in range(1, 2 * m + 1):
                max_stones = max(max_stones, suffix_sums[i] - dp(i + x, max(m, x)))
            
            return max_stones
            
        return dp(0, 1)
# Time complexity: O(n^2)