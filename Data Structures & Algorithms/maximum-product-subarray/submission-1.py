class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)

        return res


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.maxProduct(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, -3, 4], 4)
    print_and_assert([-2, -1], 2)
