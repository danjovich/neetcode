from heapq import heapify, heappop, heappush
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        indexed_flights = [[] for _ in range(n)]
        for from_i, to_i, price_i in flights:
            indexed_flights[from_i].append((price_i, to_i))

        h = [(p, t, 0) for p, t in indexed_flights[src]]
        heapify(h)
        visited = {(src, 0)}
        res = math.inf
        while h:
            p, t, s = heappop(h)
            if t == dst:
                res = min(res, p)
            elif s < k and (t, s + 1) not in visited:
                visited.add((t, s + 1))
                for p_i, t_i in indexed_flights[t]:
                    heappush(h, (p_i + p, t_i, s + 1))
        
        return int(res) if res != math.inf else -1

