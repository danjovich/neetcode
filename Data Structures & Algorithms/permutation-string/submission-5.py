from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1) - 1
        c1 = Counter(s1)
        c2 = Counter(s2[i:j + 1])

        while j < len(s2):
            if c1 == c2:
                return True
            c2[s2[i]] -= 1
            i += 1
            j += 1
            if j < len(s2):
                c2[s2[j]] += 1

        return False

    def checkInclusion_inefficient(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1)
        c1 = Counter(s1)

        while j <= len(s2):
            if c1 == Counter(s2[i:j]):
                return True
            i += 1
            j += 1
        
        return False
            
