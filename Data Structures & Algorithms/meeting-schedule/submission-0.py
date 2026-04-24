# Definition of Interval:

class Interval(object):
    def __init__(self, start: int, end: int):
        assert end > start
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        for i1 in intervals:
            for i2 in intervals:
                if i1 != i2:
                    if not (i1.end <= i2.start or i2.end <= i1.start):
                        return False

        return True


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.canAttendMeetings(inp)
        print(res)
        assert res == exp

    print_and_assert([Interval(0, 30), Interval(5, 10), Interval(15, 20)], False)
    print_and_assert([Interval(5, 8), Interval(9, 15)], True)
