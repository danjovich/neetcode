from heapq import heapify, heappop

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        h = [(s, e) for s, e in intervals]
        heapify(h)
        remove = 0
        last_e = None

        while h:
            s, e = heappop(h)

            while h and h[0][0] < e:
                remove += 1
                s_next, e_next = heappop(h)
                if e_next < e:
                    s, e = s_next, e_next

            if last_e and last_e > s:
                remove += 1
            else:
                last_e = e

        return remove            
