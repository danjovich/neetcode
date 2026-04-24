class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # better solution (hash-sets!!! - O(n) in both space and time):
        values_found = set()
        for num in nums:
            if num in values_found: # O(1) for hash sets!
                return True
            values_found.add(num)
        return False
        
        # old solution (O(n²), although (O(1) in space)):
        #
        # for i in range(len(nums)): # n times
        #     if nums.index(nums[i]) != i: # index is O(n/2) on average
        #         return True
        # return False