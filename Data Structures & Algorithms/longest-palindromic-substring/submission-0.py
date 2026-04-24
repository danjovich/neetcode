from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        letters_indexes = defaultdict(list)
        
        for i, l in enumerate(s):
            letters_indexes[l].append(i)

        longest = "" if len(s) == 0 else s[0]
        for i, l in enumerate(s):
            letters_indexes[l] = letters_indexes[l][1:]
            for j in reversed(letters_indexes[l]):
                curr = s[i:j+1]
                if len(curr) <= len(longest):
                    continue
                found = True
                left, right = i, j
                while left < right:
                    if s[left] != s[right]:
                        found = False
                        break
                    left += 1
                    right -= 1
                if found:
                    longest = curr
        
        return longest

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.longestPalindrome(inp)
        print(res)
        assert res == exp

    print_and_assert("babad", "bab")
    print_and_assert("cbbd", "bb")
    print_and_assert("a", "a")
    print_and_assert("aacabdkacaa", "aca")
