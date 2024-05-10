class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        low, high = 0, 1
        result = [0, 1]

        while high - low > 1e-9:
            mid = (low + high) / 2
            count = 0
            max_fraction = [0, 1]

            for i in range(len(arr) - 1, -1, -1):
                j = i + 1
                while j < len(arr) and arr[i] > mid * arr[j]:
                    j += 1
                if j < len(arr) and max_fraction[0] / max_fraction[1] < arr[i] / arr[j]:
                    max_fraction = [arr[i], arr[j]]
                count += len(arr) - j

            if count < k:
                low = mid
            else:
                result = max_fraction
                high = mid

        return result