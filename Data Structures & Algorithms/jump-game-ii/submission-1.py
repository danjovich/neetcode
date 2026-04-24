class Solution:
    def jump(self, nums: list[int]) -> int:
        i = 0
        jumps = 0
        while i < len(nums) - 1:
            num = nums[i]
            if i + num >= len(nums) - 1:
                return jumps + 1
            max_jump = 0
            next = i
            for j in range(1, num + 1):
                jump = i + j + nums[i + j]
                if jump >= len(nums) - 1:
                    return jumps + 2
                if jump > max_jump:
                    next = i + j
                    max_jump = jump
            i = next
            jumps += 1
        return jumps


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.jump(inp)
        print(res)
        assert res == exp

    print_and_assert([2, 4, 1, 1, 1, 1], 2)
    print_and_assert([2, 1, 2, 1, 0], 2)
    print_and_assert([1, 2], 1)
