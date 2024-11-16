class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def isAscSorted(arr):
            for i in range(1, len(arr)):
                if arr[i]-1 != arr[i-1]:
                    return False
            return True
        resArr = []
        for i in range(0,len(nums)-k+1):
            if isAscSorted(nums[i:i+k]):
                resArr.append(max(nums[i:i+k]))
            else:
                resArr.append(-1)
        return resArr