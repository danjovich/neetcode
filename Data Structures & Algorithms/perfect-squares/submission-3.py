class Solution:
    def numSquares(self, n: int) -> int:
        squares = []

        for i in range(n):
            square = (i + 1) ** 2
            if square > n:
                break
            squares.append(square)

        dp = {}
        def recurse(curr: int, target: int):
            if (res := dp.get(target)) is not None:
                return res

            res = n
            for square in reversed(squares):
                if square > target:
                    continue
                if square == target:
                    res = 1
                    break

                res = min(res, 1 + recurse(curr + 1, target - square))

            dp[target] = res
            return res
        return recurse(0, n)