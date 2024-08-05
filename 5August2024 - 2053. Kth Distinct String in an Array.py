class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = []
        for ele in arr:
            
            if arr.count(ele) == 1:
                unique.append(ele)
            if len(unique) >= k:
                return unique[k-1]
        return ""

# Time complexity: O(n^2) because we iterate through the arr list and count the number of occurrences of each element in the arr list.