class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(curr_i_s: int, curr_i_t: int) -> int:
            if curr_i_t == len(t):
                return 1
            
            if curr_i_s == len(s):
                return 0
            
            res = 0
            for i_s in range(curr_i_s, len(s)):
                if s[i_s] == t[curr_i_t]:
                    res += dfs(i_s + 1, curr_i_t + 1)

            return res
        
        return dfs(0, 0)

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(s, t, exp):
        res = sol.numDistinct(s, t)
        print(res)
        assert res == exp

    print_and_assert("caaat", "cat", 3)
    print_and_assert("xxyxy", "xy", 5)
