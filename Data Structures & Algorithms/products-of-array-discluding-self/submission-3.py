class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)

        for i in range(1, len(nums)):
            output[i] = nums[i - 1] * output[i - 1]

        curr = 1
        for i in range(len(nums) - 2, -1, -1):
            curr *= nums[i + 1]
            output[i] *= curr

        return output


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.productExceptSelf(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 4, 6], [48, 24, 12, 8])
    print_and_assert([-1, 0, 1, 2, 3], [0, -6, 0, 0, 0])
