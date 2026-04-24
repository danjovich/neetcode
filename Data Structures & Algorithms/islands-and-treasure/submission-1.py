class Solution:
    INF = 2147483647

    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if len(grid) == 0:
            return

        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            if visited[i][j]:
                return grid[i][j]

            if grid[i][j] == -1:
                return self.INF

            if grid[i][j] == 0:
                return 0

            visited[i][j] = True

            top = dfs(i - 1, j) if i > 0 else self.INF
            right = dfs(i, j + 1) if j < n - 1 else self.INF
            bottom = dfs(i + 1, j) if i < m - 1 else self.INF
            left = dfs(i, j - 1) if j > 0 else self.INF

            res = min(top, right, bottom, left)
            if res != self.INF:
                grid[i][j] = res + 1

            return grid[i][j]

        for i in range(m):
            for j in range(n):
                visited = [[False for _ in range(n)] for _ in range(m)]
                dfs(i, j)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        sol.islandsAndTreasure(inp)
        print(inp)
        assert inp == exp

    print_and_assert(
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ],
        [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
    )
    print_and_assert([[0, -1], [2147483647, 2147483647]], [[0, -1], [1, 2]])
    print_and_assert(
        [
            [2147483647, 0, 2147483647, 2147483647, 2147483647],
            [2147483647, 2147483647, -1, 2147483647, 2147483647],
            [2147483647, 2147483647, 2147483647, -1, 2147483647],
            [0, 2147483647, -1, 2147483647, 2147483647],
            [2147483647, 2147483647, 2147483647, 0, 2147483647],
        ],
        [
            [1, 0, 1, 2, 3],
            [2, 1, -1, 3, 4],
            [1, 2, 3, -1, 3],
            [0, 1, -1, 1, 2],
            [1, 2, 1, 0, 1],
        ],
    )
