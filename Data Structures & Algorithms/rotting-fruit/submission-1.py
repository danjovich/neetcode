class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fruits = [
            (i, j)
            for i in range(len(grid))
            for j in range(len(grid[i]))
            if grid[i][j] in {1, 2}
        ]
        rotten = [(i, j, 1) for i, j in fruits if grid[i][j] == 2]
        total_rotten = len(rotten)

        time = 0
        while rotten:
            if total_rotten == len(fruits):
                return time

            i, j, time = rotten.pop(0)
            for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if k >= 0 and l >= 0 and k < len(grid) and l < len(grid[k]):
                    if grid[k][l] == 1:
                        grid[k][l] = 2
                        rotten.append((k, l, time + 1))
                        total_rotten += 1

        return time if total_rotten == len(fruits) else -1


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.orangesRotting(inp)
        print(res)
        assert res == exp

    print_and_assert([[1, 1, 0], [0, 1, 1], [0, 1, 2]], 4)
    print_and_assert([[1, 0, 1], [0, 2, 0], [1, 0, 1]], -1)
    print_and_assert([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4)
