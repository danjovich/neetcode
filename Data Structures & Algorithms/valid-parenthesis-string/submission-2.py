class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = dict()
        def dfs(i: int, l: int) -> bool:
            if i == len(s):
                return l == 0
            
            if (res := dp.get((i, l))) is not None:
                return res

            if s[i] == "(":
                dp[(i, l)] = dfs(i + 1, l + 1)
                return dp[(i, l)]
            
            if s[i] == ")":
                if l > 0 and dfs(i + 1, l - 1):
                    dp[(i, l)] = True
                    return dp[(i, l)]
                
                dp[(i, l)] = False
                return dp[(i, l)]

            if l > 0 and dfs(i + 1, l - 1):
                dp[(i, l)] = True
                return dp[(i, l)]
            
            dp[(i, l)] = dfs(i + 1, l + 1) or dfs(i + 1, l)
            return dp[(i, l)]
        return dfs(0, 0)
            
