# 840. Magic Squares In Grid
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSq(square):
            nums = [num for row in square for num in row]
            if sorted(nums) != list(range(1, 10)):
                return False
            magicNum = sum(square[0])
            if sum(square[1]) != magicNum or sum(square[2]) != magicNum:
                return False # check rows
            if square[0][0] + square[1][0] + square[2][0] != magicNum:
                return False # col 1
            if square[0][1] + square[1][1] + square[2][1] != magicNum:
                return False # col 2
            if square[0][2] + square[1][2] + square[2][2] != magicNum:
                return False # col 3
            if square[0][0] + square[1][1] + square[2][2] != magicNum:
                return False # diag 1
            if square[0][2] + square[1][1] + square[2][0] != magicNum:
                return False # diag 2
            return True
        count = 0
        
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                matrix = [row[j:j+3] for row in grid[i:i+3]]
                if isMagicSq(matrix) is True:
                    count += 1
                #print(matrix)
        return count
    
# Time complexity: O(m*n)