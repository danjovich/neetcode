class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(nums: list[int], target: int, exp: int):
        res = sol.search(nums, target)
        print(res)
        assert res == exp

    print_and_assert([3, 4, 5, 6, 1, 2], 1, 4)
    print_and_assert([3, 5, 6, 0, 1, 2], 4, -1)
    print_and_assert([4, 5, 6, 7, 0, 1, 2], 0, 4)
