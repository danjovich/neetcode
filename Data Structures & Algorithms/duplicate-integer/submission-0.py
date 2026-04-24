class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if nums.index(nums[i]) != i:
                return True
        return False