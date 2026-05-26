from heapq import heapify, heappop

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = [(s, e) for s, e in intervals]
        heapify(h)

        res, i = [], -1
        while h:
            s, e = heappop(h)
            if i >= 0 and res[i][1] >= s:
                res[i][1] = max(res[i][1], e)
            else:
                i += 1
                res.append([s, e])
        
        return res