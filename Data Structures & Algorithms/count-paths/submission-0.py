class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        cache: list[list[int | None]] = [[None] * n for _ in range(m)]

        def uniquePaths(m: int, n: int) -> int:
            if m == 1 or n == 1:
                return 1

            if cache[m - 1][n - 1] is not None:
                return cache[m - 1][n - 1]  # type: ignore

            down = uniquePaths(m - 1, n)
            right = uniquePaths(m, n - 1)

            cache[m - 1][n - 1] = down + right
            return down + right

        return uniquePaths(m, n)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(m: int, n: int, exp: int):
        res = sol.uniquePaths(m, n)
        print(res)
        assert res == exp

    print_and_assert(3, 6, 21)
