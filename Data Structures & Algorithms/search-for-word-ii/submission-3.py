from collections import defaultdict


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie: dict[str | bool, dict | None] = defaultdict(lambda: None)
        for i, word in enumerate(words):
            curr = trie
            for c in word:
                if curr[c] is None:  # type: ignore
                    curr[c] = defaultdict(lambda: None)  # type: ignore
                curr = curr[c]  # type: ignore
            curr[True] = i  # type: ignore

        res = set()

        def recurse(i: int, j: int, curr: dict, visited: set):
            if (i, j) in visited:
                return

            if type(curr[True]) is int:
                res.add(curr[True])

            t, b = i - 1, i + 1
            if t >= 0 and (nxt := curr[board[t][j]]) is not None:
                recurse(t, j, nxt, visited.union({(i, j)}))
            if b < len(board) and (nxt := curr[board[b][j]]) is not None:
                recurse(b, j, nxt, visited.union({(i, j)}))

            l, r = j - 1, j + 1
            if l >= 0 and (nxt := curr[board[i][l]]) is not None:
                recurse(i, l, nxt, visited.union({(i, j)}))
            if r < len(board[0]) and (nxt := curr[board[i][r]]) is not None:
                recurse(i, r, nxt, visited.union({(i, j)}))

        for i in range(len(board)):
            for j in range(len(board[i])):
                c = board[i][j]
                if (curr := trie[c]) is not None:
                    recurse(i, j, curr, set())

        return [words[i] for i in res]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(board, words, exp):
        res = sol.findWords(board, words)
        print(res)
        assert set(res) == set(exp)

    print_and_assert(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["oath", "pea", "eat", "rain", "hklf", "hf"],
        ["eat", "hf", "hklf", "oath"],
    )
    print_and_assert([["a", "b"]], ["ab"], ["ab"])
    print_and_assert([["a"]], ["a"], ["a"])
    print_and_assert(
        [
            ["a", "b", "c", "d"],
            ["s", "a", "a", "t"],
            ["a", "c", "k", "e"],
            ["a", "c", "d", "n"],
        ],
        ["bat", "cat", "back", "backend", "stack"],
        ["cat", "back", "backend"],
    )
    print_and_assert(
        [["x", "o"], ["x", "o"]],
        ["xoxo"],
        [],
    )
