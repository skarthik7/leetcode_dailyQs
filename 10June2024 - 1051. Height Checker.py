class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        out = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                out += 1
        return out