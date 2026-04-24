class Solution:
    dp = {}

    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        
        if word1 == word2:
            return 0

        if (val := self.dp.get((word1, word2))) is not None:
            return val

        i, j = 0, 0
        while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            i += 1
            j += 1

        if (i == len(word1) or j == len(word2)):
            self.dp[(word1, word2)] = abs(len(word1) - len(word2))
            return self.dp[(word1, word2)]

        insert = self.minDistance(word2[j] + word1[i:], word2[j:])
        delete = self.minDistance(word1[i + 1 :], word2[j:])
        replace = self.minDistance(word2[j] + word1[i + 1 :], word2[j:])

        self.dp[(word1, word2)] = 1 + min(insert, delete, replace)
        return self.dp[(word1, word2)]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(word1, word2, exp):
        res = sol.minDistance(word1, word2)
        print(res)
        assert res == exp

    print_and_assert("monkeys", "money", 2)
    print_and_assert("neatcdee", "neetcode", 3)
