class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            can_merge = False
            if 10 <= int(s[i : i + 2]) <= 26:
                can_merge = True

            dp[i] = dp[i + 1]
            if can_merge:
                dp[i] += dp[i + 2]
        return dp[0]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.numDecodings(inp)
        print(res)
        assert res == exp

    print_and_assert("12", 2)
    print_and_assert("10", 1)
    print_and_assert("1234", 3)
    print_and_assert("1214", 5)
    print_and_assert("01", 0)
