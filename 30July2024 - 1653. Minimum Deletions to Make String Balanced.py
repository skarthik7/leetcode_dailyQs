class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_a = s.count('a')
        min_deletions = float('inf')
        count_b = 0
        
        for char in s:
            if char == 'a':
                count_a -= 1
            else:
                count_b += 1
            
            min_deletions = min(min_deletions, count_a + count_b)
        
        return min_deletions

# Time complexity: O(n) because we iterate through the string once.