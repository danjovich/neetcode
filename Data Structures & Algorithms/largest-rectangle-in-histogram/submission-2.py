from typing import Tuple


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # better solution: O(n) because the while runs at
        # most n times
        stack: list[Tuple[int, int]] = []
        max_area = 0

        for i, height in enumerate([*heights, 0]):
            j, last_h = stack[-1] if stack else (i, height)
            height_index = i
            while stack and (last_h > height):
                area = (i - j) * last_h
                max_area = max(max_area, area)
                stack.pop()
                height_index = j
                if stack:
                    j, last_h = stack[-1]
            stack.append((height_index, height))

        return max_area

        # # initial solution: O(n^2) time, O(n) space
        # rectangles: list[int] = []

        # i = 0
        # while i < len(heights):
        #     curr_rectangle = heights[i]
        #     curr_height = heights[i]
        #     j = i + 1
        #     while j < len(heights):
        #         if heights[j] < curr_height:
        #             rectangles.append(curr_rectangle)
        #             curr_height = heights[j]
        #             curr_rectangle = curr_height * (j - i + 1)
        #         else:
        #             curr_rectangle += curr_height
        #         j += 1
        #     i += 1
        #     rectangles.append(curr_rectangle)

        # return max(rectangles)


if __name__ == "__main__":
    sol = Solution()

    heights = [7, 1, 7, 2, 2, 4]
    res = sol.largestRectangleArea(heights)
    print(res)
    assert res == 8

    heights = [7, 1, 7, 2, 2, 4, 8]
    res = sol.largestRectangleArea(heights)
    print(res)
    assert res == 10

    heights = [1, 3, 7]
    res = sol.largestRectangleArea(heights)
    print(res)
    assert res == 7

    heights = [2, 1, 5, 6, 2, 3]
    res = sol.largestRectangleArea(heights)
    print(res)
    assert res == 10
