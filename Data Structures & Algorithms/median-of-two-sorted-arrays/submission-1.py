class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        total = m + n
        h = (total + 1) // 2

        # edge case: nums1 is empty
        if m == 0:
            if n % 2 == 1:
                return nums2[n // 2]
            else:
                return (nums2[(n // 2) - 1] + nums2[n // 2]) / 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = h - i

            # handle cases where i or j are not in the arrays,
            # maintaining the sorted property
            nums1_l = nums1[i - 1] if i > 0 else -float("inf")
            nums1_r = nums1[i] if i < m else float("inf")
            nums2_l = nums2[j - 1] if j > 0 else -float("inf")
            nums2_r = nums2[j] if j < n else float("inf")

            # if valid partition
            if nums1_l <= nums2_r and nums2_l <= nums1_r:
                if total % 2 == 1:
                    return max(nums1_l, nums2_l)
                else:
                    return (max(nums1_l, nums2_l) + min(nums1_r, nums2_r)) / 2
            elif nums1_l > nums2_r:
                right = i - 1
            else:
                left = i + 1

        return 0


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(nums1: list[int], nums2: list[int], exp: float):
        res = sol.findMedianSortedArrays(nums1, nums2)
        print(res)
        assert res == exp

    print_and_assert([1, 3, 4, 5], [6, 7, 8, 9, 10], 6)
    print_and_assert([6, 7, 8, 9, 10], [1, 3, 4, 5], 6)
    print_and_assert([1, 3, 4, 5], [1, 2, 3], 3)
    print_and_assert([1, 3, 4, 5], [1, 2, 2], 2)
    print_and_assert([1, 2], [3], 2)
    print_and_assert([1, 3, 5, 7, 9], [2, 4], 4)
    print_and_assert([1, 2], [3, 4], 2.5)
    print_and_assert([2, 4], [1, 3], 2.5)
    print_and_assert([2, 3], [1, 4], 2.5)
    print_and_assert([1, 11, 55, 84, 102], [13, 48, 93], 51.5)
