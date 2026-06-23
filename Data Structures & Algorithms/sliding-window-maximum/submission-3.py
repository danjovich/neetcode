from heapq import heapify_max, heappop_max, heappush_max


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = [(num, i) for i, num in enumerate(nums[:k])]
        heapify_max(h)

        i = 0
        res = []
        while i + k <= len(nums):
            next_max, next_i = h[0]
            while next_i < i:
                heappop_max(h)
                next_max, next_i = h[0]
            
            res.append(next_max)
            if i + k < len(nums):
                heappush_max(h, (nums[i + k], i + k))
            i += 1

        return res
