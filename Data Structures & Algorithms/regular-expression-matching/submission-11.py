class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = dict()
        def recurse(s: str, p: str) -> bool:
            if s == p:
                return True
            
            if (res := dp.get((s, p))) is not None:
                return res

            i, j = 0, 0
            while i < len(s) and j < len(p):
                if j + 1 != len(p) and p[j + 1] == "*":
                    if s[i] == p[j] or p[j] == ".":
                        if recurse(s[i+1:], p[j:]):
                            dp[(s, p)] = True
                            return dp[(s, p)]
                    j += 2
                    continue

                if s[i] == p[j] or p[j] == ".":
                    i += 1
                    j += 1
                else:
                    dp[(s, p)] = False
                    return dp[(s, p)]
            
            if i != len(s):
                dp[(s, p)] = False
                return dp[(s, p)]

            while j < len(p):
                if j + 1 == len(p) or p[j + 1] != "*":
                    dp[(s, p)] = False
                    return dp[(s, p)]
                j += 2

            dp[(s, p)] = True
            return dp[(s, p)]
        return recurse(s, p)