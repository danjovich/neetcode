class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow, fast = 0, 0
        longest = 1 if len(s) else 0
        subs = set()

        while fast < len(s):
            c = s[fast]
            if c not in subs:
                subs.add(c)
            else:
                while s[slow] != c:
                    subs.remove(s[slow])
                    slow += 1
                slow += 1
            longest = max(longest, len(subs))
            fast += 1

        return longest


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: str, exp: int):
        res = sol.lengthOfLongestSubstring(inp)
        print(res)
        assert res == exp

    print_and_assert("zxyzxyz", 3)
    print_and_assert("xxxx", 1)
    print_and_assert("pwwkew", 3)
