class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        mn = nums[0]

        while l <= r:
            m = (r + l) // 2
            lv, mv, rv = nums[l], nums[m], nums[r]
            if mv >= rv:
                mn = min(mn, rv)
                l = m + 1
            elif mv <= lv:
                mn = min(mn, mv)
                r = m - 1
            else:
                return min(mn, lv)

        return mn


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], exp: int):
        res = sol.findMin(inp)
        print(res)
        assert res == exp

    print_and_assert([3, 4, 5, 6, 1, 2], 1)
    print_and_assert([4, 5, 0, 1, 2, 3], 0)
    print_and_assert([4, 5, 6, 7, 8, 0, 1, 2, 3, 3, 3], 0)
    print_and_assert([4, 5, 6, 7], 4)
    print_and_assert([4, 5, 6, 7, 0, 1, 2], 0)
