class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = 0
        for i, num in enumerate(nums):
            res ^= i ^ num
        return res ^ len(nums)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], exp: int):
        res = sol.missingNumber(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 3], 0)
    print_and_assert([0, 1, 2, 3, 4, 5, 6, 7, 9], 8)
