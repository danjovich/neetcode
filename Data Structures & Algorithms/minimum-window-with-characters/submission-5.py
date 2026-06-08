from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_s, dict_t = defaultdict(int), defaultdict(int)

        for c in t:
            dict_t[c] += 1

        i, j = 0, -1
        equals = 0
        res = (0, len(s))
        while i < len(s) or j < len(s):
            if j == len(s) - 1 and j - i < len(t):
                break

            if equals < len(dict_t) and j < len(s) - 1:
                j += 1

                if s[j] in dict_t:
                    dict_s[s[j]] += 1
                    if dict_s[s[j]] == dict_t[s[j]]:
                        equals += 1
            else:
                if s[i] in dict_t:
                    dict_s[s[i]] -= 1
                    if dict_s[s[i]] < dict_t[s[i]]:
                        equals -= 1

                i += 1

            if equals == len(dict_t) and j - i < res[1] - res[0]:
                res = (i, j)
                if j - i == len(t) - 1:
                    break

        i, j = res
        return s[i : j + 1] if j - i < len(s) else ""
