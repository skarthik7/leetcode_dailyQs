# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)
        
        for row in matrix:
            pattern = tuple(row)
            flipped_pattern = tuple(1 - x for x in row)
            pattern_count[pattern] += 1
            pattern_count[flipped_pattern] += 1
        
        return max(pattern_count.values())