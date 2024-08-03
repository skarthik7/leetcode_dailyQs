class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(arr) == sorted(target)
# Time complexity: O(nlogn) because we sort the target and arr lists.