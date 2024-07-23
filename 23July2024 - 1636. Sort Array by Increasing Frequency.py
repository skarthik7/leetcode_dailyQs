from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequencyDict = {}
        for ele in nums:
            frequencyDict[ele] = frequencyDict.get(ele, 0) + 1
        
        sorted_nums = sorted(nums, key=lambda x: (frequencyDict[x], -x))
        
        return sorted_nums