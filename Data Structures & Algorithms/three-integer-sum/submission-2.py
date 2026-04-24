from collections import defaultdict
from typing import Tuple


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        counts = self.initialize_count_dict(nums)
        res = set()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                num1, num2 = nums[i], nums[j]
                wanted = -(num1 + num2)
                
                count_wanted = counts[wanted] - self.count([num1, num2], wanted)
                if count_wanted > 0:
                    res.add(tuple(sorted([num1, num2, wanted])))
        
        # _, res = self.sort_and_find_three_sums(nums)

        return list(map(list, list(res)))

    def count(self, nums: list[int], target: int) -> int:
        res = 0
        for num in nums:
            if num == target:
                res += 1
        return res

    def sort_and_find_three_sums(
        self, nums: list[int]
    ) -> Tuple[list[int], set[Tuple[int, int, int]]]:
        n = len(nums)
        if n <= 1:
            return nums, set()

        left, l_sums = self.sort_and_find_three_sums(nums[: n // 2])
        right, r_sums = self.sort_and_find_three_sums(nums[n // 2 :])
        merged, split_sums = self.merge_and_fins_split_three_sums(left, right)

        return merged, l_sums.union(r_sums).union(split_sums)

    def merge_and_fins_split_three_sums(
        self, left: list[int], right: list[int]
    ) -> Tuple[list[int], set[Tuple[int, int, int]]]:
        res = []
        split_sums = set()
        i, j = 0, 0
        dict_l, dict_r = self.initialize_count_dict(left), self.initialize_count_dict(
            right
        )

        while i < len(left) and j < len(right):
            wanted = -(left[i] + right[j])
            # this is needed to avoid counting the wanted twice
            count_l = dict_l[wanted] - (1 if wanted == left[i] else 0)
            count_r = dict_r[wanted] - (1 if wanted == right[j] else 0)
            if count_l > 0 or count_r > 0:
                # we only look for split three sums as other calls
                # will have already found the non-split ones
                split_sums.add(tuple(sorted((left[i], right[j], wanted))))

            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        while i < len(left):
            res.append(left[i])
            i += 1

        while j < len(right):
            res.append(right[j])
            j += 1

        return res, split_sums

    def initialize_count_dict(self, nums: list[int]) -> defaultdict[int, int]:
        res = defaultdict(lambda: 0)
        for num in nums:
            res[num] += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], expected: list[list[int]]):
        ans = sol.threeSum(inp)
        print(ans)
        assert len(ans) == len(expected)
        for i in range(len(ans)):
            found = False
            for j in range(len(expected)):
                found = set(ans[i]) == set(expected[j])
                if found:
                    break
            assert found

    print_and_assert([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    print_and_assert([0, 1, 1], [])
    print_and_assert([0, 0, 0], [[0, 0, 0]])
    print_and_assert([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])
