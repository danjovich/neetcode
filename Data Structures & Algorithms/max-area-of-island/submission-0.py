class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        checked: set[tuple[int, int]] = set()

        def areaOfIsland(
            grid: list[list[int]],
            start: tuple[int, int],
        ) -> int:
            checked.add(start)
            i, j = start

            l = (
                areaOfIsland(grid, (i - 1, j))
                if i > 0 and grid[i - 1][j] and (i - 1, j) not in checked
                else 0
            )
            r = (
                areaOfIsland(grid, (i + 1, j))
                if i + 1 < len(grid) and grid[i + 1][j] and (i + 1, j) not in checked
                else 0
            )
            b = (
                areaOfIsland(grid, (i, j - 1))
                if j > 0 and grid[i][j - 1] and (i, j - 1) not in checked
                else 0
            )
            t = (
                areaOfIsland(grid, (i, j + 1))
                if j + 1 < len(grid[i]) and grid[i][j + 1] and (i, j + 1) not in checked
                else 0
            )

            return 1 + l + r + b + t

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in checked and grid[i][j]:
                    max_area = max(max_area, areaOfIsland(grid[::], (i, j)))

        return max_area


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.maxAreaOfIsland(inp)
        print(res)
        assert res == exp

    print_and_assert(
        [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]], 6
    )
