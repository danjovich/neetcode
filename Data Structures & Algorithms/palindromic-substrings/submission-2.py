class Solution:
    def countSubstrings(self, s: str) -> int:
        known = set()

        def testUnknownPalindrome(i: int, j: int):
            if (i, j) in known:
                return
            ss = s[i : j + 1]
            l, r = 0, len(ss) - 1

            local_prev = set()
            while l < r:
                local_prev.add((l + i, r + i))
                if ss[l] != ss[r]:
                    return
                l += 1
                r -= 1

            known.update(local_prev)

        for i, c1 in enumerate(s):
            for j in range(len(s) - 1, i, -1):
                c2 = s[j]
                if c1 == c2:
                    testUnknownPalindrome(i, j)

        return len(known) + len(s)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.countSubstrings(inp)
        print(res)
        assert res == exp

    print_and_assert("abc", 3)
    print_and_assert("aaa", 6)
    print_and_assert("aaaaa", 15)
