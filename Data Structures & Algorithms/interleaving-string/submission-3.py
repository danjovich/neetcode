class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i1: int, i2: int, i3: int):
            if i3 == len(s3):
                res = i1 == len(s1) and i2 == len(s2)
                dp[(i1, i2, i3)] = res
                return res

            res = False
            if i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3]:
                res = dfs(i1 + 1, i2, i3 + 1)

            if not res and i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3]:
                res = dfs(i1, i2 + 1, i3 + 1)

            dp[(i1, i2, i3)] = res
            return res

        return dfs(0, 0, 0)

    def isInterleaveBacktracking(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def backtrack(i1: int, i2: int, i3: int, in1: bool):
            if i3 == len(s3):
                return i1 == len(s1) and i2 == len(s2)

            if in1:
                passed = False
                while i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3]:
                    passed = True
                    i1 += 1
                    i3 += 1
                    if i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3]:
                        if backtrack(i1, i2, i3, False):
                            return True
                if not passed:
                    return False
            else:
                passed = False
                while i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3]:
                    passed = True
                    i2 += 1
                    i3 += 1
                    if i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3]:
                        if backtrack(i1, i2, i3, True):
                            return True
                if not passed:
                    return False

            return backtrack(i1, i2, i3, not in1)

        return backtrack(0, 0, 0, True) or backtrack(0, 0, 0, False)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(s1: str, s2: str, s3: str, exp):
        res = sol.isInterleave(s1, s2, s3)
        print(res)
        assert res == exp

    print_and_assert(s1="aaaa", s2="bbbb", s3="aabbbbaa", exp=True)
    print_and_assert(s1="", s2="", s3="", exp=True)
    print_and_assert(s1="", s2="", s3="a", exp=False)
    print_and_assert(s1="abc", s2="xyz", s3="abxzcy", exp=False)
    print_and_assert(s1="aa", s2="ab", s3="aaba", exp=True)
