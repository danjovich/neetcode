class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res, res_i = [0] * m * n, 0

        i, j, spirals = 0, 0, 0
        while res_i < m * n:
            res[res_i] = matrix[i][j]
            res_i += 1

            if i == spirals and j + 1 < n - spirals:
                j += 1
            elif j + 1 == n - spirals and i + 1 < m - spirals:
                i += 1
            elif i + 1 == m - spirals and j > spirals:
                j -= 1
            elif j == spirals and i > spirals:
                i -= 1
                if i == spirals + 1 and j == spirals:
                    spirals += 1
        
        return res
