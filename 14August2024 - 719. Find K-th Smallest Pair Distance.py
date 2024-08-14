class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def count_pairs_with_distance_less_than_or_equal(mid: int) -> int:
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        nums.sort()
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if count_pairs_with_distance_less_than_or_equal(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left