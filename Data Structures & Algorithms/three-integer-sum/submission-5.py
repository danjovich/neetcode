class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # TODO: is there a O(n log n) solution for this problem
        # using the counting inversions strategy?

        # this solution is O(n²) and more elegant than mine :( (below)
        nums_sorted = sorted(nums)
        res = []

        for i in range(len(nums_sorted)):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                # avoids duplicates
                continue
            j = i + 1
            k = len(nums_sorted) - 1
            while j < k:
                three_sum = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
                if three_sum == 0:
                    res.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                # the equal appears in both if's for we already checked for the
                # current i, j, k so there would only be duplicates left
                if three_sum >= 0:
                    # must decrease the sum, the while avoids duplicates
                    # (guaranteed due to array being sorted)
                    k -= 1
                    while j < k and nums_sorted[k] == nums_sorted[k + 1]:
                        k -= 1
                if three_sum <= 0:
                    # must increase the sum, the while avoids duplicates
                    # (guaranteed due to array being sorted)
                    j += 1
                    while j < k and nums_sorted[j] == nums_sorted[j - 1]:
                        j += 1

        return res

        # this solution (mine) is O(n²) and works!
        # counts = self.initialize_count_dict(nums)
        # res = set()

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         num1, num2 = nums[i], nums[j]
        #         wanted = -(num1 + num2)

        #         count_wanted = counts[wanted] - self.count([num1, num2], wanted)
        #         if count_wanted > 0:
        #             res.add(tuple(sorted([num1, num2, wanted])))

        # # _, res = self.sort_and_find_three_sums(nums)

        # return list(map(list, list(res)))

    # def count(self, nums: list[int], target: int) -> int:
    #     res = 0
    #     for num in nums:
    #         if num == target:
    #             res += 1
    #     return res

    # def initialize_count_dict(self, nums: list[int]) -> defaultdict[int, int]:
    #     res = defaultdict(lambda: 0)
    #     for num in nums:
    #         res[num] += 1
    #     return res


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
    print_and_assert([-2, 0, 0, 2, 2], [[-2, 0, 2]])
