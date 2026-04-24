class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # O(n) -> Kadane's Algorithm
        curr_sum = nums[0]
        maximum = curr_sum

        for i in range(1, len(nums)):
            # if the sum so far is negative, it won't contribute
            # to the maximum of the remaining numbers (note that
            # you shouldn't restart the sum on finding a negative
            # nums[i], as the subarray is sequential so a negative
            # number that doesn't make the sum negative is not a
            # problem)
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[i]
            maximum = max(curr_sum, maximum)

        return maximum

    def maxSubArrayNSquared(self, nums: list[int]) -> int:
        # O(n^2)
        maximum = nums[0]

        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                maximum = max(curr, maximum)

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
