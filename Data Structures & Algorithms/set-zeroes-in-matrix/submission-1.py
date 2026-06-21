class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        lines, cols = {}, {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    lines[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if lines.get(i) or cols.get(j):
                    matrix[i][j] = 0
        

        