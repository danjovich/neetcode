class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # def get_prev(nums: list[tuple[int, int]], i: int) -> int:
        #     return nums[i - 1][0] if i > 0 else 1

        # def get_next(nums: list[tuple[int, int]], i: int) -> int:
        #     return nums[i + 1][0] if i < len(nums) - 1 else 1

        # dp = {}
        # def backtrack(nums: list[tuple[int, int]], bursted: str) -> int:
        #     if (coins := dp.get(bursted)) is not None:
        #         return coins

        #     result = 0
        #     for i, (num, actual_i) in enumerate(nums):
        #         coins = get_prev(nums, i) * num * get_next(nums, i)
        #         coins += backtrack(nums[:i] + nums[i + 1 :], bursted[:actual_i] + "1" + bursted[actual_i + 1 :])
        #         result = max(result, coins)

        #     dp[bursted] = result
        #     return result

        # n = len(nums)
        # return backtrack([(nums[i], i) for i in range(n)], "0" * n)

        def get_prev(nums: list[int], i: int) -> int:
            return nums[i - 1] if i > 0 else 1

        def get_next(nums: list[int], i: int) -> int:
            return nums[i + 1] if i < len(nums) - 1 else 1

        dp = {}

        def backtrack(nums: list[int]) -> int:
            if (coins := dp.get(tuple(nums))) is not None:
                return coins

            result = 0
            for i in range(len(nums)):
                coins = get_prev(nums, i) * nums[i] * get_next(nums, i)
                coins += backtrack(nums[:i] + nums[i + 1 :])
                result = max(result, coins)

            dp[tuple(nums)] = result
            return result

        return backtrack(nums)