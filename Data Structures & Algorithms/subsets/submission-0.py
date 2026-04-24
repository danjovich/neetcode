class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(nums: list[int]) -> list[list[int]]:
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                return [nums]

            res: list[list[int]] = []

            for i, n in enumerate(nums):
                res.append([n])
                for l in backtrack(nums[i + 1 :]):
                    res.append([n] + l)

            return res

        return [[]] + backtrack(nums)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], exp: list[list[int]]):
        res = sol.subsets(inp)
        print(res)
        assert len(res) == len(exp)
        for item in res:
            assert item in exp

    print_and_assert([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    print_and_assert([7], [[], [7]])
