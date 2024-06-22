class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def countAtMostK(k):
            left = count = total = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                total += right - left + 1
            return total
        
      
        return countAtMostK(k) - countAtMostK(k - 1)