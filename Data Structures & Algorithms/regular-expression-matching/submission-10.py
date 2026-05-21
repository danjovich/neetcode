class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True

        i, j = 0, 0
        while i < len(s) and j < len(p):
            if j + 1 != len(p) and p[j + 1] == "*":
                if s[i] == p[j] or p[j] == ".":
                    if self.isMatch(s[i+1:], p[j:]):
                        return True
                j += 2
                continue

            if s[i] == p[j] or p[j] == ".":
                i += 1
                j += 1
            else:
                return False                
        
        if i != len(s):
            return False

        while j < len(p):
            if j + 1 == len(p) or p[j + 1] != "*":
                return False
            j += 2

        return True