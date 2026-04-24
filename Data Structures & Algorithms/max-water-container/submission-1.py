class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = 0

        while l < r:
            amount = min(heights[l], heights[r]) * (r - l)
            if amount > max_amount:
                max_amount = amount
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_amount


if __name__ == "__main__":
    sol = Solution()

    inp = [1, 7, 2, 5, 4, 7, 3, 6]
    out = sol.maxArea(inp)
    print(out)
    assert out == 36

    inp = [2, 2, 2]
    out = sol.maxArea(inp)
    print(out)
    assert out == 4
