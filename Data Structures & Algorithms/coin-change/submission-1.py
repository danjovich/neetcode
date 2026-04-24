class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp: list[int | None] = [None] * (amount + 1)

        def dfs(a):
            if a == 0:
                return 0

            if a < 0:
                return amount + 1

            if (val := dp[a]) is not None:
                return val

            res = amount + 1
            for coin in coins:
                res = min(res, 1 + dfs(a - coin))

            dp[a] = res
            return res

        res = dfs(amount)
        return res if res <= amount else -1


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(coins, amount, exp):
        res = sol.coinChange(coins, amount)
        print(res)
        assert res == exp

    print_and_assert([1, 5, 10], 12, 3)
    print_and_assert([1], 2, 2)
    print_and_assert([2], 3, -1)
    print_and_assert([1], 0, 0)
