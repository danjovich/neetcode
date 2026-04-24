from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time: O(n), space: O(n)
        if len(s) != len(t):
            return False

        Counter("a")

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        for key in count_s:
            if count_s[key] != count_t.get(key):
                return False

        return True

        # Original solution (time: 0(n²), space: O(1))
        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)): # n times
        #     if s.count(s[i]) != t.count(s[i]): # count is O(n)
        #         return False

        # return True

        # one-liners:
        #
        # return sorted(s) == sorted(t) # time: O(n log n), space: O(1)
        #
        # # from collections import Counter
        # return Counter(s) == Counter(t) # time and space: O(n) (same as explicit, uncommented solution)


if __name__ == "__main__":
    print(Solution().isAnagram(s="racecar", t="carrace"))
    print(Solution().isAnagram(s="jar", t="jam"))
