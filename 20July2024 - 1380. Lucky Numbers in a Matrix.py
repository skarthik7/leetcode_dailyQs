class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        col_max = [0]*len(matrix[0])
        row_min = [float('inf')]*len(matrix)
        for i in range (len(matrix)):
            row_min[i] = min(matrix[i])
            for j in range(len(matrix[i])):
                col_max[j] = max(col_max[j],matrix[i][j])
        row_min_set = set(row_min)
        col_max_set = set(col_max)


        lucky_numbers = row_min_set.intersection(col_max_set)
        return lucky_numbers

# Time Complexity: O(N*M) where N is the number of rows and M is the number of columns in the matrix.