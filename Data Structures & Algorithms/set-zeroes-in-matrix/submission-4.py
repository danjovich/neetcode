class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_first_line, zero_first_col = False, False

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zero_first_col = True
                break
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                zero_first_line = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if zero_first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if zero_first_line:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        

        