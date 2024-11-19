class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0
        
        current_sum = 0
        max_sum = 0
        window_set = set()
        left = 0
        
        for right in range(len(nums)):
            while nums[right] in window_set:
                window_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            window_set.add(nums[right])
            current_sum += nums[right]
            
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                window_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1
        
        return max_sum
    
# time complexity: O(n)