from heapq import heappop, heappush

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i : (i.start, i.end))

        h = []
        res = 0
        for interval in intervals:
            if h:
                while h and h[0] <= interval.start:
                    heappop(h)

            heappush(h, interval.end)
            res = max(res, len(h))

        return res