# 2134. Minimum Swaps to Group All 1's Together II
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        n = len(nums)
        
        extended_nums = nums + nums
        
        max_ones_in_window = 0
        current_ones_in_window = 0
        
        for i in range(total_ones):
            current_ones_in_window += extended_nums[i]
        
        max_ones_in_window = current_ones_in_window
        for i in range(total_ones, 2 * n):
            current_ones_in_window += extended_nums[i] - extended_nums[i - total_ones]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
        
        return total_ones - max_ones_in_window
