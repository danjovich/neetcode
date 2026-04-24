from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        i, j = 0, 1

        store = defaultdict(lambda: 0)
        store[s[0]] += 1
        store[s[1]] += 1

        while j < len(s):
            if k + max(store.values()) >= (j - i + 1):
                res = max(res, j - i + 1)
                j += 1
                if j == len(s):
                    break
                store[s[j]] += 1
            else:
                if store[s[i]] == 1:
                    del store[s[i]]
                else:
                    store[s[i]] -= 1
                i += 1

        return res

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(s, k, exp):
        res = sol.characterReplacement(s, k)
        print(res)
        assert res == exp

    print_and_assert("AAAA", 2, 4)
    print_and_assert("ABAA", 0, 2)
    print_and_assert("XYYX", 2, 4)
    print_and_assert("AAABABB", 1, 5)
