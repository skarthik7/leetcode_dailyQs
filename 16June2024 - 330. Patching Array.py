class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        patches = 0
        index = 0
        
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                # If the current number is within the range we can form
                # Then update miss
                miss += nums[index]
                index += 1
            else:
                # If the current number is outside the range
                # Then add miss to the array (conceptually)
                miss *= 2
                patches += 1
        
        return patches