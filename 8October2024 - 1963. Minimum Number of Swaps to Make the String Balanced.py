class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_unbalanced = 0
        
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                max_unbalanced = max(max_unbalanced, -balance)
        
        return (max_unbalanced + 1) // 2
# Time complexity: O(N)