class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = dict()

        def recurse(i: int, j: int) -> bool:
            if (res := dp.get((i, j))) is not None:
                return res

            while i < len(s) and j < len(p):
                if j + 1 != len(p) and p[j + 1] == "*":
                    if s[i] == p[j] or p[j] == ".":
                        if recurse(i + 1, j):
                            dp[(i, j)] = True
                            return dp[(i, j)]
                    j += 2
                    continue

                if s[i] == p[j] or p[j] == ".":
                    i += 1
                    j += 1
                else:
                    dp[(i, j)] = False
                    return dp[(i, j)]

            if i != len(s):
                dp[(i, j)] = False
                return dp[(i, j)]

            while j < len(p):
                if j + 1 == len(p) or p[j + 1] != "*":
                    dp[(i, j)] = False
                    return dp[(i, j)]
                j += 2

            dp[(i, j)] = True
            return dp[(i, j)]

        return recurse(0, 0)
