class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            # r + l can lead to overflow
            i = l + ((r - l) // 2)

            if nums[i] > target:
                r = i - 1
            elif nums[i] < target:
                l = i + 1
            else:
                return i
        return -1

    def recursive_search(self, nums: list[int], target: int) -> int:
        # time: O(log n), space: O(log n)
        if len(nums) == 0:
            return -1

        i = len(nums) // 2
        if nums[i] < target:
            res = self.search(nums[i + 1 :], target)
            if res < 0:
                return res
            return i + 1 + res
        if nums[i] > target:
            return self.search(nums[:i], target)
        return i


if __name__ == "__main__":
    sol = Solution()

    nums = [-1, 0, 2, 4, 6, 8]
    res = sol.search(nums, 4)
    print(res)
    assert res == 3

    nums = [-1, 0, 2, 4, 6, 8]
    res = sol.search(nums, 3)
    print(res)
    assert res == -1
