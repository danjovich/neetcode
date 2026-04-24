class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i:].startswith(word) and dp[i + len(word)]:
                    dp[i] = True

        return dp[0]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(s, wordDict, exp):
        res = sol.wordBreak(s, wordDict)
        print(res)
        assert res == exp

    print_and_assert("neetcode", ["neet", "code"], True)
    print_and_assert("applepenapple", ["apple", "pen", "ape"], True)
    print_and_assert("catsincars", ["cats", "cat", "sin", "in", "car"], False)
