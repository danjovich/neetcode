class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        def dfs(i: int, profit = 0, owns = False) -> int:
            if i >= len(prices):
                return profit
            
            if i == len(prices) - 1:
                if owns:
                    return profit + prices[i]
                return profit

            if owns:
                sell = dfs(i + 2, profit + prices[i])
                not_sell = dfs(i + 1, profit, True)
                return max(sell, not_sell)

            buy = dfs(i + 1, profit - prices[i], True)
            not_buy = dfs(i + 1, profit)

            return max(buy, not_buy)

        return dfs(0)

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.maxProfit(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 3, 4, 0, 4], 6)
    print_and_assert([1], 0)
