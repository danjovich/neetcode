class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp: dict[tuple[str, str], int] = {}

        def recurse(t1: str, t2: str) -> int:
            if not t1 or not t2:
                return 0
            if res := dp.get((t1, t2)):
                return res

            res = 0
            for i, c1 in enumerate(t1):
                for j, c2 in enumerate(t2):
                    if c1 == c2:
                        res = max(res, 1 + recurse(t1[i + 1 :], t2[j + 1 :]))
                        break

            

            dp[(t1, t2)] = res
            dp[(t2, t1)] = res
            return res

        return recurse(text1, text2)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(t1: str, t2: str, exp: int):
        res = sol.longestCommonSubsequence(t1, t2)
        print(res)
        assert res == exp

    print_and_assert("oxcpqrsvwf", "shmtulqrypy", 2)
    print_and_assert("cat", "crabt", 3)
    print_and_assert("abcd", "abcd", 4)
    print_and_assert("abcd", "efgh", 0)
