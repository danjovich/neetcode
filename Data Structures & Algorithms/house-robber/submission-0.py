class Solution:
    def rob(self, nums: list[int]) -> int:
        res: dict[int, int] = {}

        def dp(i: int) -> int:
            if len(nums) <= i:
                return 0
            if len(nums) == i + 1:
                return nums[i]
            if res.get(i) is not None:
                return res[i]

            res[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return res[i]

        return dp(0)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.rob(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 1, 3, 3], 4)
    print_and_assert([2, 9, 8, 3, 6], 16)
