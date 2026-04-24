class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i = 0
        while i < len(nums) - 1:
            length = nums[i]
            if not length:
                return False
            next_v, next_i = 0, i + 1
            for j in range(i + 1, i + length + 1):
                if j < len(nums) - 1 and nums[j] + j > next_v:
                    next_v = nums[j] + j
                    next_i = j
                elif j >= len(nums) - 1:
                    return True
            i = next_i
        return True

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.canJump(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 0, 1, 0], True)
    print_and_assert([1, 2, 1, 0, 1], False)
    print_and_assert([3,0,8,2,0,0,1], True)
