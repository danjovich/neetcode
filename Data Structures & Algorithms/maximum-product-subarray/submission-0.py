from operator import mul


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # todos positivos -> mult todos
        # há um ou mais zeros -> max entre subarrays excluindo zeros
        # há negativos (sem zeros) -> max entre subarrays contendo pares de negativos

        # res = 1
        # for num in nums:
        #     res *= num

        # l, r = 0, len(nums) - 1
        def mult(nums):
            res = 1
            for num in nums:
                res *= num
            return res

        res = max(nums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(res, mult(nums[i:j+1]))

        return res

        # res =
        # def dfs(i):
        #     if i == len(nums) - 1:
        #         return nums[i]

        #     res = 1
        #     for i in range(i, len(nums)):

        #         res = max(dfs(nums[:i]), dfs(nums[i + 1 :]))
        #         res = max(res, nums[i] * res)

        #     return res

        # def dfs(nums):
        #     if len(nums) == 1:
        #         return nums[0]

        #     l = max(mult(nums[1:]), dfs(nums[1:]))
        #     r = max(mult(nums[:-1]), dfs(nums[:-1]))

        #     return max(l, r)

        # return dfs(nums)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.maxProduct(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, -3, 4], 4)
    print_and_assert([-2, -1], 2)
