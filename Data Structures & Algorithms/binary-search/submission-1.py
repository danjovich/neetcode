class Solution:
    def search(self, nums: list[int], target: int) -> int:
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
