class Solution:
    def trap(self, heights: list[int]) -> int:
        # O(n) time, O(1) space (ideal)
        if not heights: return 0

        l, r = 0, len(heights) - 1
        max_l, max_r = heights[l], heights[r]
        total_area = 0

        while l < r:
            if heights[l] <= heights[r]:
                if heights[l] < max_l:
                    total_area += max_l - heights[l]
                elif heights[l] > max_l:
                    max_l = heights[l]

                l += 1
            else:
                if heights[r] < max_r:
                    total_area += max_r - heights[r]
                elif heights[r] > max_r:
                    max_r = heights[r]

                r -= 1

        return total_area

        # time: O(n), space: O(m), m = number of "holes",
        # m = n/2 - 1  in the worst case

        # l_start, r_start = 0, len(heights) - 1
        # l, r = l_start + 1, r_start - 1
        # l_area, r_area = 0, 0
        # total_area = 0
        # found_holes: set[tuple] = set()

        # while l < len(heights) and r >= 0:
        #     if heights[l_start] <= heights[l]:
        #         hole_tuple = (l_start, l, l_area)
        #         if hole_tuple not in found_holes:
        #             total_area += l_area
        #             found_holes.add(hole_tuple)
        #         l_area = 0
        #         l_start = l
        #     else:
        #         l_area += heights[l_start] - heights[l]

        #     if heights[r_start] <= heights[r]:
        #         hole_tuple = (r, r_start, r_area)
        #         if hole_tuple not in found_holes:
        #             total_area += r_area
        #             found_holes.add(hole_tuple)
        #         r_area = 0
        #         r_start = r
        #     else:
        #         r_area += heights[r_start] - heights[r]

        #     l += 1
        #     r -= 1

        # return total_area


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[int], expected_ans: int):
        ans = sol.trap(inp)
        print(ans)
        assert ans == expected_ans

    print_and_assert([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9)
    print_and_assert([4, 2, 3], 1)
    print_and_assert([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
