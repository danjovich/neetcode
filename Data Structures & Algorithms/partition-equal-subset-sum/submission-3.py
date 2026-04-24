class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        dp: list[bool] = [False] * (1 + total // 2)
        dp[0] = True

        for num in nums:
            for amount in range(total // 2, num - 1, -1):
                dp[amount] = dp[amount] or dp[amount - num]

        return dp[total // 2]

        # dp: list[bool | None] = [None] * (1 + total // 2)

        # def dfs(amount: int, nums: list[int]):
        #     if amount < 0:
        #         return False
        #     if amount == 0:
        #         return True
        #     if (val := dp[amount]) is not None:
        #         return val

        #     for i, num in enumerate(nums):
        #         if dfs(amount - num, nums[:i] + nums[i + 1 :]):
        #             dp[amount] = True
        #             return True
        #     dp[amount] = False
        #     return False

        # return dfs(total // 2, nums)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.canPartition(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 3, 4], True)
    print_and_assert([1, 2, 3, 4, 5], False)
    print_and_assert([1, 2, 3, 4, 12], False)
    print_and_assert([1, 2, 3, 4, 5, 7, 8], True)
    print_and_assert([1, 2, 3, 8], False)
    print_and_assert([1, 2, 5], False)
