class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        i_ended = False
        j_ended = False
        while i < len(s) and j >= 0:
            a = s[i]
            while not a.isalnum() and not i_ended:
                i += 1
                if i == len(s):
                    i_ended = True
                else:
                    a = s[i]

            b = s[j]
            while not b.isalnum() and not j_ended:
                j -= 1
                if j == -1:
                    j_ended = True
                else:
                    b = s[j]

            if i_ended and j_ended:
                return True
            elif i_ended or j_ended:
                # if one ended but the other didn't,
                # than its not a palindrome
                return False

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
