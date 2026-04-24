class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        elements = set()

        for num in nums:
            elements.add(num)

        curr_up = elements.pop()
        curr_down = curr_up
        length = 1
        longest_length = length
        found = False
        for _ in range(len(elements)):
            if curr_up + 1 in elements:
                curr_up += 1
                elements.remove(curr_up)
                length += 1
                found = True

            if curr_down - 1 in elements:
                curr_down -= 1
                elements.remove(curr_down)
                length += 1
                found = True

            if length > longest_length:
                longest_length = length

            if not found:
                length = 1
                if len(elements) == 0:
                    break
                curr_up = elements.pop()
                curr_down = curr_up
            found = False

        return longest_length


if __name__ == "__main__":
    ans = Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5])
    print(ans)
    assert ans == 4

    ans = Solution().longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1])
    print(ans)
    assert ans == 7

    ans = Solution().longestConsecutive([0, -1])
    print(ans)
    assert ans == 2

    ans = Solution().longestConsecutive([2, 11, 8, 15, 9, 4, 7, 12, 13, 14, 5, 3])
    print(ans)
    assert ans == 5
