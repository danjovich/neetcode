class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        def combinationSumTuples(
            candidates: list[int], target: int
        ) -> set[tuple[int, ...]]:
            s = sum(candidates)
            if s == target:
                return {tuple(candidates)}
            if s < target:
                return set()

            res: set[tuple[int, ...]] = set()
            for i in range(len(candidates)):
                combs = combinationSumTuples(
                    candidates[:i] + candidates[i + 1 :], target
                )
                res = res.union(combs)

            return res

        return list(map(list, combinationSumTuples(candidates, target)))


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(nums: list[int], target: int, exp: list[list[int]]):
        res = sol.combinationSum2(nums, target)
        print(res)
        assert len(res) == len(exp)
        for r in res:
            valid = False
            for e in exp:
                if len(r) != len(e):
                    continue
                equal_items = True
                for item in r:
                    if r.count(item) != e.count(item):
                        equal_items = False
                        break
                if equal_items:
                    valid = True
                    break
        assert valid

    print_and_assert([9, 2, 2, 4, 6, 1, 5], 8, [[1, 2, 5], [2, 2, 4], [2, 6]])
    print_and_assert([1, 2, 3, 4, 5], 7, [[1, 2, 4], [2, 5], [3, 4]])
    print_and_assert([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
