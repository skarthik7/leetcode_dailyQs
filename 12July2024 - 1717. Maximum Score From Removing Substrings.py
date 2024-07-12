class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        if x > y:
            first, second, first_points, second_points = "ab", "ba", x, y
        else:
            first, second, first_points, second_points = "ba", "ab", y, x
        
        def remove_substring_and_calculate_points(s: str, sub: str, points: int) -> (str, int):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] + char == sub:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score
        
        modified_s, score = remove_substring_and_calculate_points(s, first, first_points)
        _, additional_score = remove_substring_and_calculate_points(modified_s, second, second_points)
        
        return score + additional_score
    
# Time complexity: O(N) as we iterate through the string once where N is the length of the string.