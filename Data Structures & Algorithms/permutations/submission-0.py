class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]

        res: list[list[int]] = []
        for i, num in enumerate(nums):
            for perm in self.permute(nums[:i] + nums[i + 1 :]):
                res.append([num] + perm)

        return res


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.permute(inp)
        print(res)
        assert len(res) == len(exp)

    print_and_assert(
        [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )

    print_and_assert(
        [1, 2, 3, 4],
        [
            [1, 2, 3, 4],
            [1, 3, 2, 4],
            [2, 1, 3, 4],
            [2, 3, 1, 4],
            [3, 1, 2, 4],
            [3, 2, 1, 4],
            [1, 2, 4, 3],
            [1, 3, 4, 2],
            [2, 1, 4, 3],
            [2, 3, 4, 1],
            [3, 1, 4, 2],
            [3, 2, 4, 1],
            [1, 4, 2, 3],
            [1, 4, 3, 2],
            [2, 4, 1, 3],
            [2, 4, 3, 1],
            [3, 4, 1, 2],
            [3, 4, 2, 1],
            [4, 1, 2, 3],
            [4, 1, 3, 2],
            [4, 2, 1, 3],
            [4, 2, 3, 1],
            [4, 3, 1, 2],
            [4, 3, 2, 1],
        ],
    )
