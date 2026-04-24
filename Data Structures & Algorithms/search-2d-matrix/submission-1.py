class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def searchMatrix(
            start=0,
            end=m * n,
        ) -> bool:
            if start == end:
                return False

            mid = start + (end - start) // 2
            i, j = mid // n, mid % n

            if end - start == 1:
                i_end, j_end = end // n, end % n
                return matrix[i][j] == target or (
                    i_end < m and j_end < n and matrix[i_end][j_end] == target
                )

            if matrix[i][j] < target:
                return searchMatrix(mid, end)
            elif matrix[i][j] > target:
                return searchMatrix(start, mid)

            return True

        return searchMatrix()


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(matrix: list[list[int]], target: int, exp: bool):
        res = sol.searchMatrix(matrix, target)
        print(res)
        assert res == exp

    print_and_assert([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10, True)
    print_and_assert([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15, False)
    print_and_assert([[1]], 0, False)
    print_and_assert([[1]], 1, True)
