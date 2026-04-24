class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def backtrack(nums: list[int]) -> list[list[int]]:
            if len(nums) == 0:
                return []
            if len(nums) == 1:
                return [nums]

            sol: list[list[int]] = []
            last = None
            for i, num in enumerate(nums):
                if num == last:
                    continue
                last = num
                sol.append([num])
                for res in backtrack(nums[i + 1 :]):
                    sol.append([num] + res)

            return sol

        return [[]] + backtrack(sorted(nums))


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], exp: list[list[int]]):
        res = sol.subsetsWithDup(inp)
        print(res)
        assert len(res) == len(exp)
        res = [sorted(arr) for arr in res]
        exp = [sorted(arr) for arr in exp]
        for item in res:
            assert item in exp

    print_and_assert([1, 2, 1], [[], [1], [1, 2], [1, 1], [1, 2, 1], [2]])
    print_and_assert([7, 7], [[], [7], [7, 7]])
