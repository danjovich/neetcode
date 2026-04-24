class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max_amount = 0

        for l in range(len(heights)):
            for r in range(l, len(heights)):
                amount = min(heights[l], heights[r]) * (r - l)
                if amount > max_amount:
                    max_amount = amount

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
