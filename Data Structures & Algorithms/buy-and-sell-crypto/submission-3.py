class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # sliding window (like two-pointers, but not from right to left)
        # O(n), O(1)
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                # if is profitable, calculate profit
                profit = max(profit, prices[r] - prices[l])
            else:
                # if not, we found a new optimal buying time
                # (and we checked every possible profit before
                # this buying point)
                l = r
            # always increment selling point to check for 
            # every profitable possibility for each buy
            r += 1

        return profit

    def maxProfitInitialSolution(self, prices: list[int]) -> int:
        # not sure, but seems O(n)
        profit = 0
        max_p, max_p_i = 0, 0

        i = 0
        while i + 1 < len(prices):
            while prices[i] > prices[i + 1]:
                i += 1
                if i + 1 == len(prices):
                    return profit

            if i >= max_p_i:
                j = i + 1
                max_p, max_p_i = prices[j], j
                while j < len(prices):
                    if prices[j] > max_p:
                        max_p = prices[j]
                        max_p_i = j
                    j += 1

            curr_profit = max_p - prices[i]
            profit = max(profit, curr_profit)
            i += 1

        return profit


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], exp: int):
        res = sol.maxProfit(inp)
        print(res)
        assert res == exp

    print_and_assert([10, 1, 5, 6, 7, 1], 6)
    print_and_assert([10, 8, 7, 5, 2], 0)
    print_and_assert([2, 1, 2, 0, 1], 1)
