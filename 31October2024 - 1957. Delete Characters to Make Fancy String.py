class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        
        for char in s:
            if len(result) >= 2 and result[-1] == result[-2] == char:
                continue
            result.append(char)
        
        return ''.join(result)
# Time complexity: O(n) 
# where n is the number of characters in the string