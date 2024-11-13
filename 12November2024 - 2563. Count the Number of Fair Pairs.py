class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search_left(target, start):
            left, right = start, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
            
        def binary_search_right(target, start):
            left, right = start, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        nums.sort()
        count = 0
        
        for i in range(len(nums)):
            left = binary_search_left(lower - nums[i], i + 1)
            right = binary_search_right(upper - nums[i], i + 1)
            
            if left <= right:
                count += right - left + 1  
        return count