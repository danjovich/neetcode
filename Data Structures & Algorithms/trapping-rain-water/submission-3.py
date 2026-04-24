class Solution:
    def trap(self, heights: list[int]) -> int:
        l_start, r_start = 0, len(heights) - 1
        l, r = l_start + 1, r_start - 1
        l_area, r_area = 0, 0
        total_area = 0
        found_holes: set[tuple] = set()

        while l < len(heights) and r >= 0:
            if heights[l_start] <= heights[l]:
                hole_tuple = (l_start, l, l_area)
                if hole_tuple not in found_holes:
                    total_area += l_area
                    found_holes.add(hole_tuple)
                l_area = 0
                l_start = l
            else:
                l_area += heights[l_start] - heights[l]

            if heights[r_start] <= heights[r]:
                hole_tuple = (r, r_start, r_area)
                if hole_tuple not in found_holes:
                    total_area += r_area
                    found_holes.add(hole_tuple)
                r_area = 0
                r_start = r
            else:
                r_area += heights[r_start] - heights[r]

            l += 1
            r -= 1

        return total_area


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], expected_ans: int):
        ans = sol.trap(inp)
        print(ans)
        assert ans == expected_ans

    print_and_assert([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9)
    print_and_assert([4, 2, 3], 1)
    print_and_assert([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
