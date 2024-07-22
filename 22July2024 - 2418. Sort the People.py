from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = zip(names, heights)
        sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=True)
        sorted_names = [name for name, height in sorted_pairs]
        return sorted_names
# Time Complexity: O(NlogN) where N is the number of people.