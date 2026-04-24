class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        checked = [False for _ in strs]
        result = []

        for i in range(len((strs))):
            if checked[i]:
                continue

            curr = [strs[i]]
            checked[i] = True
            for j in range(len(strs)):
                if checked[j]:
                    continue

                if self.isAnagram(strs[i], strs[j]):
                    curr.append(strs[j])
                    checked[j] = True

            result.append(curr)

        return result

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s.count(s[i]) != t.count(s[i]):
                return False

        return True
