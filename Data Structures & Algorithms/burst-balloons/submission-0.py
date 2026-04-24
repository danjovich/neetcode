class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        def get_prev(i: int, ignore: str) -> int:
            for prev in range(i - 1, -1, -1):
                if ignore[prev] == "0":
                    return nums[prev]
            return 1

        def get_next(i: int, ignore: str) -> int:
            for next in range(i + 1, len(nums)):
                if ignore[next] == "0":
                    return nums[next]
            return 1

        dp = {}
        def backtrack(bursted: str) -> int:
            if (coins := dp.get(bursted)) is not None:
                return coins

            result = 0
            for i, num in enumerate(nums):
                if bursted[i] == "0":
                    coins = get_prev(i, bursted) * nums[i] * get_next(i, bursted)
                    coins += backtrack(bursted[:i] + "1" + bursted[i + 1 :])
                    result = max(result, coins)

            dp[bursted] = result
            return result

        return backtrack(len(nums) * "0")