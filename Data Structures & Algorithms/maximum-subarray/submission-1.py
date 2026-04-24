class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maximum = nums[0]

        for i in range(1, len(nums) + 1):
            j = 0
            while j + i <= len(nums):
                curr = sum(nums[j:j+i])
                maximum = max(curr, maximum)
                j += 1
        
        return maximum

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.maxSubArray(inp)
        print(res)
        assert res == exp

    print_and_assert([2, -3, 4, -2, 2, 1, -1, 4], 8)
    print_and_assert([-1], -1)
    print_and_assert([5, 4, -1, 7, 8], 23)
