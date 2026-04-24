import math


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for i1 in range(math.ceil(n / 2)):
            for j1 in range(i1, n - 1 - i1):
                i2, j2 = j1, n - 1 - i1
                i3, j3 = j2, n - 1 - i2
                i4, j4 = j3, n - 1 - i3
                matrix[i1][j1], matrix[i2][j2], matrix[i3][j3], matrix[i4][j4] = (
                    matrix[i4][j4],
                    matrix[i1][j1],
                    matrix[i2][j2],
                    matrix[i3][j3],
                )


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        sol.rotate(inp)
        print(inp)
        assert inp == exp

    print_and_assert([[1, 2], [3, 4]], [[3, 1], [4, 2]])
    print_and_assert(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    )
    print_and_assert(
        [[5, 1, 9, 11],
         [2, 4, 8, 10],
         [13, 3, 6, 7],
         [15, 14, 12, 16]],
        
        [[15, 13, 2, 5],
         [14, 3, 4, 1],
         [12, 6, 8, 9],
         [16, 7, 10, 11]],
        
    )
