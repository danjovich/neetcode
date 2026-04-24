class Solution:
    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        if n == 0:
            return []
        if n == 1:
            return [[s]]

        res: list[list[str]] = []

        for i in range(n):
            ss = s[: i + 1]
            if self.isPalindrome(ss):
                if len(ss) == len(s):
                    res.append([ss])
                    continue

                curr = []
                for p in self.partition(s[i + 1 :]):
                    curr = [ss] + p
                    res.append(curr)

        return res

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return False
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.partition(inp)
        print(res)
        assert res == exp

    print_and_assert("aab", [["a", "a", "b"], ["aa", "b"]])
    print_and_assert("a", [["a"]])
    print_and_assert("bb", [["b", "b"], ["bb"]])
    print_and_assert("cdd", [["c", "d", "d"], ["c", "dd"]])
