class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)

        res = 1
        for i in range(len(nums) - 1, -1, -1):
            curr = dp[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    curr = max(curr, 1 + dp[j])
            dp[i] = curr
            res = max(res, curr)

        return res


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.lengthOfLIS(inp)
        print(res)
        assert res == exp

    print_and_assert([9, 1, 4, 2, 3, 3, 7], 4)
    print_and_assert([0, 3, 1, 3, 2, 3], 4)
