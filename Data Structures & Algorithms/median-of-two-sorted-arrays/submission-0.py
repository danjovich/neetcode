class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the shorter array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        # Handle edge case where one array is empty
        if m == 0:
            if n % 2 == 1:
                return nums2[n // 2]
            else:
                return (nums2[(n // 2) - 1] + nums2[n // 2]) / 2

        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = half - i

            # Handle cases where partitions are at the edges
            nums1_left = nums1[i - 1] if i > 0 else -float("inf")
            nums1_right = nums1[i] if i < m else float("inf")
            nums2_left = nums2[j - 1] if j > 0 else -float("inf")
            nums2_right = nums2[j] if j < n else float("inf")

            # Check if partitions are valid
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (
                        max(nums1_left, nums2_left) + min(nums1_right, nums2_right)
                    ) / 2
            elif nums1_left > nums2_right:
                high = i - 1
            else:
                low = i + 1

        return 0.0  # This return is theoretically unreachable with valid inputs