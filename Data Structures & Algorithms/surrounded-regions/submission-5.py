from collections import deque
from typing import Optional


class Solution:

    def solve(self, board: list[list[str]]) -> None:
        q = deque(maxlen=len(board) * len(board[0]))

        for i in range(len(board)):
            if board[i][0] == "O":
                q.append((i, 0))

            if board[i][-1] == "O":
                q.append((i, len(board[i]) - 1))

        for j in range(1, len(board[0]) - 1):
            if board[0][j] == "O":
                q.append((0, j))

            if board[-1][j] == "O":
                q.append((len(board) - 1, j))

        while q:
            i, j = q.popleft()

            board[i][j] = "N"  # not surrounded

            if i > 0 and board[i - 1][j] == "O":
                q.append((i - 1, j))

            if i < len(board) - 1 and board[i + 1][j] == "O":
                q.append((i + 1, j))

            if j > 0 and board[i][j - 1] == "O":
                q.append((i, j - 1))

            if j < len(board[i]) - 1 and board[i][j + 1] == "O":
                q.append((i, j + 1))

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "N":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def solve_memory_unoptimized(self, board: list[list[str]]) -> None:
        not_surrounded = set()

        def dfs(i: int, j: int, visited: set) -> Optional[bool]:
            assert board[i][j] == "O"

            visited.add((i, j))

            unknown = False
            for k, l in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                if (k, l) in not_surrounded:
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
                        not_surrounded.add((i, j))
                        return False

                    if (res := dfs(k, l, visited.copy())) is True:
                        board[i][j] = "X"
                        return True
                    elif res is False:
                        not_surrounded.add((i, j))
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
