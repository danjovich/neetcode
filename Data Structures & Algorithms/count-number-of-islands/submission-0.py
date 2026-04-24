class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        nodes: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    nodes.add((i, j))

        def dfs(pair: tuple[int, int]):
            if pair in nodes:
                nodes.remove(pair)
            i, j = pair

            u, r, d, l = (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)

            for node in [u, r, d, l]:
                if node in nodes:
                    dfs(node)

        islands = 0
        while nodes:
            dfs(nodes.pop())
            islands += 1

        return islands


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.numIslands(inp)
        print(res)
        assert res == exp

    print_and_assert(
        [
            ["0", "1", "1", "1", "0"],
            ["0", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    )

    print_and_assert(
        [
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        4,
    )
