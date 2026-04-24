class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_histogram_s = {}
        letters_histogram_t = {}
        for i in range(len(s)):
            letters_histogram_s[s[i]] = (
                letters_histogram_s[s[i]] + 1 if letters_histogram_s.get(s[i]) else 1
            )
            letters_histogram_t[t[i]] = (
                letters_histogram_t[t[i]] + 1 if letters_histogram_t.get(t[i]) else 1
            )

        if len(letters_histogram_s.keys()) != len(letters_histogram_t.keys()):
            return False

        for key in letters_histogram_s.keys():
            if not letters_histogram_t.get(key):
                return False

            if letters_histogram_s[key] != letters_histogram_t[key]:
                return False

        return True