from collections import defaultdict


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        if amount == 0:
            return 1

        coins = sorted(coins)
        dp = defaultdict(dict)

        def backtrack(a: int, i: int) -> int:
            if (val := dp[a].get(i)) is not None:
                return val
            count = 0
            for j in range(i, len(coins)):
                coin = coins[j]
                if coin < a:
                    count += backtrack(a - coin, j)
                elif coin == a:
                    count += 1
                if coin >= a:
                    break

            dp[a][i] = count
            return count

        return backtrack(amount, 0)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(amount, coins, exp):
        res = sol.change(amount, coins)
        print(res)
        assert res == exp

    print_and_assert(4, [1, 2, 3], 4)
    print_and_assert(7, [2, 4], 0)
