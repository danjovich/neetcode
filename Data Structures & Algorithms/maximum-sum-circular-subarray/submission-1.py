class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(n):
            curr_sum = nums[i]
            res = max(res, curr_sum)
            j = (i + 1) % n
            while j != i:
                curr_sum += nums[j]
                res = max(res, curr_sum)
                j = (j + 1) % n


        return res
            
            