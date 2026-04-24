from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # time: O(m * n), space: O(n)

        map_of_freqs_to_words = defaultdict(list)

        for s in strs: # n times (strs len)
            freqs = [0] * 26
            for c in s: # m times (average s len)
                freqs[ord(c) - ord("a")] += 1
            # tuples are hashable!!
            map_of_freqs_to_words[tuple(freqs)].append(s)

        return map_of_freqs_to_words.values()

    # def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #     # O(n²*m)
    #     # indexes not yet analyzed
    #     unchecked = set(range(len(strs)))
    #     result = []

    #     for i in range(len((strs))): # n times
    #         if i not in unchecked:
    #             continue

    #         curr = [strs[i]]
    #         unchecked.remove(i)
    #         for j in unchecked.copy(): # n/2 times on worst case
    #             if self.isAnagram(strs[i], strs[j]): # O(m) call
    #                 curr.append(strs[j])
    #                 unchecked.remove(j)

    #         result.append(curr)

    #     return result

    # def isAnagram(self, s: str, t: str) -> bool:
    #     # time: O(n), space: O(n)
    #     if len(s) != len(t):
    #         return False

    #     count_s, count_t = {}, {}
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # time: O(m * n), space: O(n)

        map_of_freqs_to_words = defaultdict(list)

        for s in strs: # n times (strs len)
            freqs = [0] * 26
            for c in s: # m times (average s len)
                freqs[ord(c) - ord("a")] += 1
            # tuples are hashable!!
            map_of_freqs_to_words[tuple(freqs)].append(s)

        return map_of_freqs_to_words.values()

    # def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #     # O(n²*m)
    #     # indexes not yet analyzed
    #     unchecked = set(range(len(strs)))
    #     result = []

    #     for i in range(len((strs))): # n times
    #         if i not in unchecked:
    #             continue

    #         curr = [strs[i]]
    #         unchecked.remove(i)
    #         for j in unchecked.copy(): # n/2 times on worst case
    #             if self.isAnagram(strs[i], strs[j]): # O(m) call
    #                 curr.append(strs[j])
    #                 unchecked.remove(j)

    #         result.append(curr)

    #     return result

    # def isAnagram(self, s: str, t: str) -> bool:
    #     # time: O(n), space: O(n)
    #     if len(s) != len(t):
    #         return False

    #     count_s, count_t = {}, {}

    #     for i in range(len(s)):
    #         count_s[s[i]] = 1 + count_s.get(s[i], 0)
    #         count_t[t[i]] = 1 + count_t.get(t[i], 0)

    #     for key in count_s:
    #         if count_s[key] != count_t.get(key):
    #             return False

    #     return True


if __name__ == "__main__":
    print(Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
    print(Solution().groupAnagrams(["x"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["", ""]))

    #     for i in range(len(s)):
    #         count_s[s[i]] = 1 + count_s.get(s[i], 0)
    #         count_t[t[i]] = 1 + count_t.get(t[i], 0)

    #     for key in count_s:
    #         if count_s[key] != count_t.get(key):
    #             return False

    #     return True


if __name__ == "__main__":
    print(Solution().groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
    print(Solution().groupAnagrams(["x"]))
    print(Solution().groupAnagrams([""]))
    print(Solution().groupAnagrams(["", ""]))
