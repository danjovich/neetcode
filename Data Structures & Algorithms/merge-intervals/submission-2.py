from heapq import heapify, heappop

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapify(intervals)

        res, i = [], -1
        while intervals:
            s, e = heappop(intervals)
            if i >= 0 and res[i][1] >= s:
                res[i][1] = max(res[i][1], e)
            else:
                i += 1
                res.append([s, e])
        
        return res