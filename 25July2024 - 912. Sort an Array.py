from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_array = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            
            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])
            
            return sorted_array
        
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        return merge(left_half, right_half)


# Time complexity: O(nlogn) - Merge sort - as required..