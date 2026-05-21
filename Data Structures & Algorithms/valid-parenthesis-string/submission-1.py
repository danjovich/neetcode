class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = dict()
        def recurse(i: int, l: int) -> bool:
            if i == len(s):
                return l == 0
            
            if (res := dp.get((i, l))) is not None:
                return res

            if s[i] == "(":
                dp[(i, l)] = recurse(i + 1, l + 1)
                return dp[(i, l)]
            
            if s[i] == ")":
                if l > 0 and recurse(i + 1, l - 1):
                    dp[(i, l)] = True
                    return dp[(i, l)]
                
                dp[(i, l)] = False
                return dp[(i, l)]

            if l > 0 and recurse(i + 1, l - 1):
                dp[(i, l)] = True
                return dp[(i, l)]
            
            dp[(i, l)] = recurse(i + 1, l + 1) or recurse(i + 1, l)
            return dp[(i, l)]
        return recurse(0, 0)

            # while i < len(s) and (s[i] != "*" or l >= 0):
            #     if s[i] == "(":
            #         l += 1
            #     elif s[i] == ")":
            #         l -= 1
            #     else:
            #         a -= 1
            #         l += 1
            #     i += 1
            
            # if i == len(s):
            #     return l >= 0 and l == a
            
            # if l < 0 and s[i] != "*":
            #     return False
            
            # return recurse()
            
