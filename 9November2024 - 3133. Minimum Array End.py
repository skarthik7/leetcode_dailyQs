# https://leetcode.com/problems/minimum-array-end/
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        remaining = n - 1
        position = 1
    
        while remaining:
            if not (x & position):
                res |= (remaining & 1) * position
                remaining >>= 1
            position <<= 1
    
        return res
