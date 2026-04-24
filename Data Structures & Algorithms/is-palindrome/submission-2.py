class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n) in time - O(2n), in fact - and O(1) in space
        i = 0
        j = len(s) - 1
        while i < len(s) and j >= 0:
            a = s[i]
            while not a.isalnum():
                i += 1
                # it is not necessary to go to the end since j
                # already checked it
                if i > len(s) // 2:
                    return True
                a = s[i]

            b = s[j]
            while not b.isalnum():
                j -= 1
                # it is not necessary to go to the start since i
                # already checked it
                if j < len(s) // 2:
                    return True
                b = s[j]

            if a.lower() != b.lower():
                return False

            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    sol = Solution()

    assert sol.isPalindrome("Was it a car or a cat I saw?")
    assert not sol.isPalindrome("tab a cat")
    assert sol.isPalindrome(" ")
