class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() 
        count = 0
        n = len(nums)
        
        for i in range(n):
            left = i + 1
            while left < n and nums[i] + nums[left] < lower:
                left += 1
                
            right = n - 1
            while right > i and nums[i] + nums[right] > upper:
                right -= 1
                
            if left <= right and right > i:
                count += right - left + 1
                
        return count