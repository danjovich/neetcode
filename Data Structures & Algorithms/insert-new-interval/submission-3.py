class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        n_start, n_end = newInterval
        for i, interval in enumerate(intervals):
            i_start, i_end = interval
            if i_start > n_start and i_start > n_end:
                return intervals[:i] + [newInterval] + intervals[i:]
            elif i_end >= n_start:
                j = i
                j_start, j_end = intervals[j]
                while j < len(intervals) - 1:
                    if intervals[j + 1][0] > n_end:
                        break
                    j += 1
                    j_start, j_end = intervals[j]
                start = min(i_start, n_start)
                if j == len(intervals) - 1:
                    end = max(n_end, j_end)
                    return intervals[:i] + [[start, end]]
                end = max(n_end, intervals[j][1])
                return intervals[:i] + [[start, end]] + intervals[j + 1 :]
        return intervals + [newInterval]


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(intervals, newInterval, exp):
        res = sol.insert(intervals, newInterval)
        print(res)
        assert res == exp

    print_and_assert([[1, 3], [4, 6]], [2, 5], [[1, 6]])
    print_and_assert([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]])
    print_and_assert(
        [[1, 2], [3, 5], [9, 10]], [6, 7], [[1, 2], [3, 5], [6, 7], [9, 10]]
    )
    print_and_assert(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        [4, 8],
        [[1, 2], [3, 10], [12, 16]],
    )
