from collections import defaultdict
import math
import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist, prev = [math.inf] * (n + 1), [0] * (n + 1)
        edges = defaultdict(list)
        for time in times:
            ui, vi, ti = time
            edges[ui].append((vi, ti))

        dist[k] = 0
        h = dist[1:]
        heapq.heapify(h)
        visited = [False] * (n + 1)

        while h:
            tu = heapq.heappop(h)
            u = [v for v in range(1, n + 1) if dist[v] == tu and not visited[v]][0]
            visited[u] = True

            for edge in edges[u]:
                vi, ti = edge
                if dist[vi] > dist[u] + ti:
                    d = dist[vi]
                    dist[vi] = dist[u] + ti
                    prev[vi] = u
                    # update heap
                    i = h.index(d)
                    h[i] = dist[vi]
                    heapq.heapify(h)
        dist = dist[1:]
        return int(max(dist)) if max(dist) < math.inf else -1


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(times: list[list[int]], n: int, k: int, exp: int):
        res = sol.networkDelayTime(times, n, k)
        print(res)
        assert res == exp

    print_and_assert([[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], 4, 1, 3)
    print_and_assert([[1, 2, 1], [2, 3, 1]], 3, 2, -1)
    print_and_assert([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2)
