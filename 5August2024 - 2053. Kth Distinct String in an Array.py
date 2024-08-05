
# Two solutions listed below; one is naive - O(n^2) and the other is optimized - O(n).

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


# Optimized solution:
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for ele in arr:
            if ele in count:
                count[ele] += 1
            else:
                count[ele] = 1
        
        unique = [ele for ele in arr if count[ele] == 1]
        
        if len(unique) >= k:
            return unique[k-1]
        return ""
# Time complexity: O(n) because we iterate through the arr list once and count the number of occurrences of each element in the arr list.