class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        rectangles: list[int] = []

        i = 0
        while i < len(heights):
            curr_rectangle = heights[i]
            curr_height = heights[i]
            j = i + 1
            while j < len(heights):
                if heights[j] < curr_height:
                    rectangles.append(curr_rectangle)
                    curr_height = heights[j]
                    curr_rectangle = curr_height * (j - i + 1)
                else:
                    curr_rectangle += curr_height
                j += 1
            i += 1
            rectangles.append(curr_rectangle)

        return max(rectangles)


if __name__ == "__main__":
    sol = Solution()

    heights = [7, 1, 7, 2, 2, 4]
    res = sol.largestRectangleArea(heights)
    print(res)
    assert res == 8

    heights = [1, 3, 7]
    res = sol.largestRectangleArea(heights)
    print(res)
    assert res == 7
