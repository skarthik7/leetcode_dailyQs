class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = deque(), deque()
        left = 0
        for right, num in enumerate(nums):
            while maxq and num > maxq[-1]:
                maxq.pop()
            while minq and num < minq[-1]:
                minq.pop()
            maxq.append(num)
            minq.append(num)
            if maxq[0] - minq[0] > limit:
                if maxq[0] == nums[left]:
                    maxq.popleft()
                if minq[0] == nums[left]:
                    minq.popleft()
                left += 1
        return right - left + 1