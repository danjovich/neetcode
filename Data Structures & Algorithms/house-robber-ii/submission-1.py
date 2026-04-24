class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = {}

        def recurse(i: int, visits_first: bool = False) -> int:
            if i >= len(nums):
                return 0
            if res := dp.get((i, visits_first)):
                return res

            if visits_first and i == len(nums) - 1:
                including_i = 0
            else:
                including_i = nums[i] + recurse(i + 2, i == 0 or visits_first)
            skipping_i = recurse(i + 1, visits_first)

            dp[(i, visits_first)] = max(including_i, skipping_i)
            return dp[(i, visits_first)]

        return recurse(0)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], exp: int):
        res = sol.rob(inp)
        print(res)
        assert res == exp

    print_and_assert([3, 4, 3], 4)
    print_and_assert([2, 9, 8, 3, 6], 15)
