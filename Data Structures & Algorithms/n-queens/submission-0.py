class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res_cols = []

        def dfs(invalid_cols: list[int], row: int = 0):
            if row == n:
                res_cols.append(invalid_cols)
                return

            for col in range(n):
                is_invalid = False
                for invalid_row, invalid_col in enumerate(invalid_cols):
                    if invalid_col == col or (
                        abs(invalid_row - row) == abs(invalid_col - col)
                    ):
                        is_invalid = True
                        break

                if not is_invalid:
                    dfs(invalid_cols + [col], row + 1)

        dfs([])

        res = []
        for cols in res_cols:
            res_row = []
            for col in cols:
                res_row.append("." * col + "Q" + "." * (n - col - 1))
            res.append(res_row)

        return res


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.solveNQueens(inp)
        print(res)
        assert res == exp

    print_and_assert(
        4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    )
    print_and_assert(1, [["Q"]])
