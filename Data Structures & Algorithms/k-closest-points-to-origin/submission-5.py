import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap: list[tuple[float, list[int]]] = []

        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            if len(heap) < k or -dist > heap[0][0]:
                if len(heap) >= k:
                    heapq.heappushpop(heap, (-dist, [x, y]))
                else:
                    heapq.heappush(heap, (-dist, [x, y]))

        return [point for _, point in heap]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(points: list[list[int]], k: int, exp: list[list[int]]):
        res = sol.kClosest(points, k)
        print(res)
        assert sorted(res) == sorted(exp)

    print_and_assert([[0, 2], [2, 2]], 1, [[0, 2]])
    print_and_assert([[0, 2], [2, 0], [2, 2]], 2, [[0, 2], [2, 0]])
    print_and_assert([[-5, 4], [-6, -5], [4, 6]], 2, [[-5, 4], [4, 6]])
