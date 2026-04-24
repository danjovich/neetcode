class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        while n != 1:
            temp = n
            res = 0
            while temp:
                res += (temp % 10) ** 2
                temp //= 10

            if res in seen_nums:
                return False

            seen_nums.add(res)
            n = res
        return True


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: int, exp: bool):
        res = sol.isHappy(inp)
        print(res)
        assert res == exp

    print_and_assert(100, True)
    print_and_assert(101, False)
