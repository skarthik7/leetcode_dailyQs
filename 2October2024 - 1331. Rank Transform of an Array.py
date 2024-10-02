class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        sort_a = sorted(list(set(arr)))       
        
        for i in range(len(sort_a)):
            ranks[sort_a[i]] = i+1
          
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr