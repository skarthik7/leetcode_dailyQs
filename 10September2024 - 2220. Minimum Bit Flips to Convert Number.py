class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # Step 1: XOR the two numbers
        xor_result = start ^ goal
        
        # Step 2: Count the number of 1s in the XOR result
        count = 0
        while xor_result:
            count += xor_result & 1
            xor_result >>= 1
        
        return count

# time complexity: O(n)