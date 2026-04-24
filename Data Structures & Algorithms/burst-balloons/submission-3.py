class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        dp = {}

        def dfs(start: int, end: int) -> int:
            # if end == 0 or start == len(nums):
            #     return 0

            if start > end:
                return 0

            if (res := dp.get((start, end))) is not None:
                return res

            res = 0
            for i in range(start, end + 1):
                coins = nums[i]
                # The trick here is to think `i`` will be the LAST one
                # to be popped, instead of the first! That's why we
                # look at the indexes before start and after end,
                # and not before and after i (these multiplications would
                # then actually happen in the end when there's only
                # start - 1, i and end + 1 left)
                coins *= nums[start - 1] if start > 0 else 1
                coins *= nums[end + 1] if end < len(nums) - 1 else 1
                coins += dfs(start, i - 1) + dfs(i + 1, end)
                res = max(res, coins)

            dp[(start, end)] = res
            return dp[(start, end)]

        return dfs(0, len(nums) - 1)