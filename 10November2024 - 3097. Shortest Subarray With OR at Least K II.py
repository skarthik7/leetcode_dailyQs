class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_length = float('inf')
        left = 0
        
        for right in range(n):
            current_or = 0
            for i in range(left, right + 1):
                current_or |= nums[i]
            
            while current_or >= k and left <= right:
                min_length = min(min_length, right - left + 1)
                left += 1
                current_or = 0
                for i in range(left, right + 1):
                    current_or |= nums[i]
        
        return min_length if min_length != float('inf') else -1