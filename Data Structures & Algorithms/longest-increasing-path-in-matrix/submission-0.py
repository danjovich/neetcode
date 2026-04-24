class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        dp = [[0 for _ in matrix[i]] for i in range(len(matrix))]

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
                return 0

            if dp[i][j] != 0:
                return dp[i][j]

            res = 1
            for tup in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                k, l = tup
                if k < 0 or k >= len(matrix) or l < 0 or l >= len(matrix[k]):
                    continue
                if matrix[k][l] < matrix[i][j]:
                    res = max(res, 1 + dfs(k, l))

            dp[i][j] = res
            return res

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, dfs(i, j))
        
        return res

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.longestIncreasingPath(inp)
        print(res)
        assert res == exp

    print_and_assert([[5, 5, 3], [2, 3, 6], [1, 1, 1]], 4)
    print_and_assert([[1, 2, 3], [2, 1, 4], [7, 6, 5]], 7)
