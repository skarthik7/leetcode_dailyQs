class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        result = []
        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])
        
        return result