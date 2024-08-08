class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]   # Directions: right, down, left, up
        output = [[rStart, cStart]]
        x, y = rStart, cStart
        steps = 1
        
        while len(output) < rows * cols:
            for i in range(4):
                dx, dy = directions[i]
                for _ in range(steps):
                    x += dx
                    y += dy
                    if 0 <= x < rows and 0 <= y < cols:
                        output.append([x, y])

                if i % 2 == 1:
                    steps += 1
        
        return output
    
# Time complexity: O(max(rows, cols)^2)