class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        unique = []
        for ele in arr:
            
            if arr.count(ele) == 1:
                unique.append(ele)
            if len(unique) >= k:
                return unique[k-1]
        return ""