class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i: int, j: int) -> bool:
            if obstacleGrid[i][j] == 1:
                return 0

            if dp[i][j] > 0:
                return dp[i][j]

            if i == m - 1 and j == n - 1:
                return 1

            if i != m - 1:
                dp[i][j] += dfs(i + 1, j)

            if j != n - 1:
                dp[i][j] += dfs(i, j + 1)

            return dp[i][j]

        return dfs(0, 0)
