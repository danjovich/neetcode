class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            expected = target - nums[i]
            try:
                j = nums.index(expected)
                if i == j:
                    continue
                return sorted([i, j])
            except ValueError:
                pass

        return []