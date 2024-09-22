class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix: int, n: int) -> int:
            current = prefix
            next_prefix = prefix + 1
            count = 0
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count
        
        current = 1
        k -= 1 
        
        while k > 0:
            count = count_prefix(current, n)
            if count <= k:
                k -= count
                current += 1
            else:
                current *= 10
                k -= 1
        
        return current