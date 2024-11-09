# https://leetcode.com/problems/minimum-array-end/
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        nums = [x]
        current = x
        for i in range(1, n):
            next_val = current + 1
            while (next_val & x) != x:
                next_val += 1
            nums.append(next_val)
            current = next_val
        
        return nums[-1]