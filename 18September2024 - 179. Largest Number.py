class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        nums_str.sort(key=lambda x: x*10, reverse=True)
        if nums_str[0] == '0':
            return '0'
        return ''.join(nums_str)
 # Time complexity: O(nlogn)