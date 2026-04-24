from typing import Optional

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        not_sorrounded = set()

        def dfs(i: int, j: int, top_level = True) -> Optional[bool]:
            assert board[i][j] == "O"

            if (
                (i - 1 == 0 and board[i - 1][j] == "O")
                or (i - 1, j) in not_sorrounded
                or (j - 1 == 0 and board[i][j - 1] == "O")
                or (i, j - 1) in not_sorrounded
            ):
                not_sorrounded.add((i, j))
                return False

            for k, l in [(i, j + 1), (i + 1, j)]:
                if (k, l) in not_sorrounded:
                    return False

                if board[k][l] == "O":
                    if k == len(board) - 1 or l == len(board[k]) - 1:
                        not_sorrounded.add((i, j))
                        return False

                    if (res := dfs(k, l, False)) is True:
                        board[i][j] = "X"
                        return True
                    elif res is False:
                        not_sorrounded.add((i, j))
                        return False
                    
            if top_level:
                board[i][j] = "X"
                return True

            return None

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if board[i][j] == "O":
                    dfs(i, j)

    def solve_unoptimized(self, board: list[list[str]]) -> None:
        not_sorrounded = set()

        def dfs(i: int, j: int, visited: set) -> Optional[bool]:
            assert board[i][j] == "O"

            visited.add((i, j))

            unknown = False
            for k, l in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                if (k, l) in not_sorrounded:
                    return False

                if (k, l) in visited:
                    unknown = True
                    continue

                if board[k][l] == "O":
                    if (
                        k == 0
                        or k == len(board) - 1
                        or l == 0
                        or l == len(board[k]) - 1
                    ):
                        not_sorrounded.add((i, j))
                        return False

                    if (res := dfs(k, l, visited.copy())) is True:
                        board[i][j] = "X"
                        return True
                    elif res is False:
                        not_sorrounded.add((i, j))
                        return False

            if not unknown:
                board[i][j] = "X"
                return True

            return None

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if board[i][j] == "O":
                    dfs(i, j, set())


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        sol.solve(inp)
        print(inp)

        equal = True
        for i in range(len(inp)):
            for j in range(len(inp[i])):
                if inp[i][j] != exp[i][j]:
                    equal = False
                    print("Different from expected at: ({}, {})".format(i, j))
        assert equal

    print_and_assert(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "X", "O"],
        ],
        [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "O"],
        ],
    )
    print_and_assert(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ],
        [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ],
    )
    print_and_assert(
        [
            ["O", "X", "X", "O", "X"],
            ["X", "O", "O", "X", "O"],
            ["X", "O", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"],
        ],
        [
            ["O", "X", "X", "O", "X"],
            ["X", "X", "X", "X", "O"],
            ["X", "X", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"],
        ],
    )
    print_and_assert(
        [
            ["X", "O", "X", "O", "X", "O", "O", "O", "X", "O"],
            ["X", "O", "O", "X", "X", "X", "O", "O", "O", "X"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
            ["O", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
            ["O", "O", "X", "X", "O", "X", "X", "O", "O", "O"],
            ["X", "O", "O", "X", "X", "X", "O", "X", "X", "O"],
            ["X", "O", "X", "O", "O", "X", "X", "O", "X", "O"],
            ["X", "X", "O", "X", "X", "O", "X", "O", "O", "X"],
            ["O", "O", "O", "O", "X", "O", "X", "O", "X", "O"],
            ["X", "X", "O", "X", "X", "X", "X", "O", "O", "O"],
        ],
        [
            ["X", "O", "X", "O", "X", "O", "O", "O", "X", "O"],
            ["X", "O", "O", "X", "X", "X", "O", "O", "O", "X"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
            ["O", "O", "O", "O", "O", "O", "X", "O", "O", "X"],
            ["O", "O", "X", "X", "O", "X", "X", "O", "O", "O"],
            ["X", "O", "O", "X", "X", "X", "X", "X", "X", "O"],
            ["X", "O", "X", "X", "X", "X", "X", "O", "X", "O"],
            ["X", "X", "O", "X", "X", "X", "X", "O", "O", "X"],
            ["O", "O", "O", "O", "X", "X", "X", "O", "X", "O"],
            ["X", "X", "O", "X", "X", "X", "X", "O", "O", "O"],
        ],
    )
