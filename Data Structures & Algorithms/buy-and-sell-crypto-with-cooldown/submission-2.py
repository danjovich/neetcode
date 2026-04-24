from collections import defaultdict


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp: dict[int, dict[int, int | None]] = defaultdict(
            lambda: defaultdict(lambda: None)
        )

        def dfs(i: int, owns=False) -> int:
            if (res := dp[i][owns]) is not None:
                return res

            if i >= len(prices):
                return 0

            if i == len(prices) - 1:
                if owns:
                    return prices[i]
                return 0

            if owns:
                sell = prices[i] + dfs(i + 2)
                not_sell = dfs(i + 1, True)
                res = dp[i][owns] = max(sell, not_sell)
                return res

            buy = dfs(i + 1, True) - prices[i]
            not_buy = dfs(i + 1)

            res = dp[i][owns] = max(buy, not_buy)
            return res

        return dfs(0)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.maxProfit(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 3, 4, 0, 4], 6)
    print_and_assert([1], 0)
