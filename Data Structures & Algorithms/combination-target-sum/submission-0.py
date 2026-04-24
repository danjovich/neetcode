class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        def combinationSum(nums: tuple[int, ...], target: int) -> set[tuple[int, ...]]:
            if sum(nums) == target:
                return {nums}

            res = set()
            for i in range(len(nums)):
                curr = nums[:i] + nums[i + 1 :]
                res = res.union(combinationSum(curr, target))

                if nums[i] < target:
                    m = 2
                    while nums[i] * m < target:
                        combs = [
                            [nums[i]] * m + list(tup)
                            for tup in combinationSum(nums, target - nums[i] * m)
                        ]
                        res = res.union(set([tuple(sorted(l)) for l in combs]))
                        m += 1
                    if nums[i] * m == target:
                        res.add(tuple([nums[i]] * m))

            return res

        return [list(tup) for tup in combinationSum(tuple(nums), target)]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(nums: list[int], target: int, exp: list[list[int]]):
        res = sol.combinationSum(nums, target)
        print(res)
        assert len(res) == len(exp)

    print_and_assert([2, 5, 6, 9], 9, [[2, 2, 5], [9]])
    print_and_assert(
        [3, 4, 5], 16, [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]
    )
