class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = [{} for _ in range(len(nums))]

        def dfs(i: int, curr: int):
            if i == len(nums):
                return 1 if curr == target else 0

            if (val := dp[i].get(curr)) is not None:
                return val

            dp[i][curr] = dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
            return dp[i][curr]

        return dfs(0, 0)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(nums, target, exp):
        res = sol.findTargetSumWays(nums, target)
        print(res)
        assert res == exp

    print_and_assert([2, 2, 2], 2, 3)
