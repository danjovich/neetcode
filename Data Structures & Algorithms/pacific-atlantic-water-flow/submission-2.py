from typing import Literal


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        dp = {}

        def dfs(i: int, j: int, equals: set | None = None) -> Literal[0, 1, 2, 3]:
            if (val := dp.get((i, j))) is not None:
                return val

            is_pac = i == 0 or j == 0
            is_atl = i == len(heights) - 1 or j == len(heights[0]) - 1

            if is_pac and is_atl:
                dp[(i, j)] = 3
                return 3

            curr = 1 if is_pac else 2 if is_atl else 0

            for k, l in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                if k >= 0 and k < len(heights) and l >= 0 and l < len(heights[k]):
                    if equals and (k, l) in equals:
                        continue
                    
                    is_equal = heights[k][l] == heights[i][j]
                    equals_set = {(i, j)} if is_equal else None
                    if (
                        heights[k][l] <= heights[i][j]
                        and (val := dfs(k, l, equals_set)) != 0
                    ):
                        if curr == 0 and val != 3:
                            curr = val
                        elif val == 3 or val != curr:
                            dp[(i, j)] = 3
                            if is_equal:
                                dp[(k, l)] = 3
                            return 3

            dp[(i, j)] = curr
            return curr

        for i in range(len(heights)):
            for j in range(len(heights[i])):
                dfs(i, j)

        return [[i, j] for i, j in dp if dp[(i, j)] == 3]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.pacificAtlantic(inp)
        print(res)

        res = {(i, j) for i, j in res}
        exp = {(i, j) for i, j in exp}

        assert len(res) == len(exp)
        for val in res:
            assert val in exp, f"Value {val} not expected"

    print_and_assert(
        [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]],
        [[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]],
    )
    print_and_assert([[1], [1]], [[0, 0], [1, 0]])
    print_and_assert(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    )
