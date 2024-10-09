class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_balance = 0
        right_balance = 0
        for char in s:
            if char == '(':
                left_balance += 1
            elif char == ')':
                if left_balance > 0:
                    left_balance -= 1
                else:
                    right_balance += 1
        
        return left_balance + right_balance

# Time complexity: O(N)