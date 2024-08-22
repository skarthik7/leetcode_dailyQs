# 476. Number Complement
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        len_binary_str = len(str(binary))
        ones = (1 << len_binary_str) - 1
        return ones-num
    
# Time complexity: O(1)