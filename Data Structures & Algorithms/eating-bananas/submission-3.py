from math import ceil


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            totalTime = 0
            k = ((r - l) // 2) + l
            for p in piles:
                totalTime += ceil(p / k)
            if totalTime > h:
                l = k + 1
            else:
                res = k
                r = k - 1

        return res


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(piles: list[int], h: int, exp: int):
        res = sol.minEatingSpeed(piles, h)
        print(res)
        assert res == exp

    print_and_assert([1, 4, 3, 2], 9, 2)
    print_and_assert([25, 10, 23, 4], 4, 25)
    print_and_assert([25, 10, 24, 4], 5, 24)
    print_and_assert([1, 4, 3, 2], 9, 2)
