class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])

        i, j, spirals = 0, 0, 0
        while len(res) < m * n:
            res.append(matrix[i][j])

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
