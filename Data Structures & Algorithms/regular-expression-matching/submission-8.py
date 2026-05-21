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
            





        # if s == p:
        #     return True

        # i, j = 0, 0
        # while i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == "." or (j + 1 < len(p) and p[j + 1] == "*")):
        #     i += 1
        #     j += 1

        #     if j < len(p) and p[j] == "*":
        #         if s[i - 1] != p[j - 1] and p[j - 1] != ".":
        #             i -= 1
        #             j += 1
        #             continue

        #         if i < len(s) and (s[i] == p[j - 1] or p[j - 1] == ".") and self.isMatch(s[i:], p[j - 1 :]):
        #             return True
        #         j += 1


        # return i == len(s) and (j == len(p) or (j + 1 == len(p) - 1 and p[j + 1] == "*"))
