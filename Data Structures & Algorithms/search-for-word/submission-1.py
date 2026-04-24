class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        cache = {}

        def backtrack(
            i: int, j: int, word_i: int, visited: set[tuple[int, int]]
        ) -> bool:
            if board[i][j] != word[word_i] or (i, j) in visited:
                return False

            if word_i == len(word) - 1:
                return True

            if res := cache.get((i, j, word_i)):
                return res

            top = (
                backtrack(i - 1, j, word_i + 1, visited.union({(i, j)}))
                if i > 0
                else False
            )
            right = (
                backtrack(i, j + 1, word_i + 1, visited.union({(i, j)}))
                if j + 1 < len(board[i])
                else False
            )
            bottom = (
                backtrack(i + 1, j, word_i + 1, visited.union({(i, j)}))
                if i + 1 < len(board)
                else False
            )
            left = (
                backtrack(i, j - 1, word_i + 1, visited.union({(i, j)}))
                if j > 0
                else False
            )

            cache[(i, j, word_i)] = top or right or bottom or left

            return cache[(i, j, word_i)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0, set()):
                    return True

        return False


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(board: list[list[str]], word: str, exp: bool):
        res = sol.exist(board, word)
        print(res)
        assert res == exp

    print_and_assert(
        [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]], "CAT", True
    )
    print_and_assert(
        [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]], "BAT", False
    )
    print_and_assert(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCB",
        False,
    )
