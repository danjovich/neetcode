from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1)
        c1 = Counter(s1)

        while j <= len(s2):
            if c1 == Counter(s2[i:j]):
                return True
            i += 1
            j += 1
        
        return False
            
