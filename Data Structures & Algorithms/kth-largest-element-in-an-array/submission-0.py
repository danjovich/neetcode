import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = [-num for num in nums]
        heapq.heapify(h)
        largest = 0
        for _ in range(k):
            largest = heapq.heappop(h)

        return -largest

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(nums, k, exp):
        res = sol.findKthLargest(nums, k)
        print(res)
        assert res == exp

    print_and_assert([2, 3, 1, 5, 4], 2, 4)
    print_and_assert([2, 3, 1, 1, 5, 5, 4], 3, 4)
