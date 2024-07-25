from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num: int) -> int:
            mapped_str = ''.join(str(mapping[int(digit)]) for digit in str(num))
            return int(mapped_str)
        
        mapped_nums = [(map_number(num), num) for num in nums]
        
        mapped_nums.sort(key=lambda x: x[0])
        
        sorted_nums = [num for _, num in mapped_nums]
        return sorted_nums