class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # to allow early-break inside the loop
        nums.sort()
        dp = {}

        def recurse(curr_target: int) -> int:
            if (res := dp.get(curr_target)) is not None:
                return res

            res = 0
            for i in range(len(nums)):
                if nums[i] >= curr_target:
                    if nums[i] == curr_target:
                        res += 1
                    break
                else:
                    res += recurse(curr_target - nums[i])

            dp[curr_target] = res
            return res

        return recurse(target)
