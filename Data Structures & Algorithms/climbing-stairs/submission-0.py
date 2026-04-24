class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp: int, exp: int):
        res = sol.climbStairs(inp)
        print(res)
        assert res == exp

    print_and_assert(2, 2)
    print_and_assert(3, 3)
