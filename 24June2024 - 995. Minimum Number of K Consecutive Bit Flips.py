from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = 0
        flipQueue = deque()
        for i in range(len(nums)):
            if flipQueue and flipQueue[0] == i:
                flipQueue.popleft()
            if len(flipQueue) % 2 == nums[i]:
                if i + k > len(nums):
                    return -1
                flips += 1
                flipQueue.append(i + k)
        return flips