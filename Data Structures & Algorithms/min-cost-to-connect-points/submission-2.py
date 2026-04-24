import math


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Altered Prim's Algorithm: O(n^2)

        n, node = len(points), 0
        dist = [math.inf] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            next_node = -1
            for i in range(n):
                if visit[i]:
                    continue
                (xi, yi), (xj, yj) = points[i], points[node]
                curr = abs(xi - xj) + abs(yi - yj)
                dist[i] = min(dist[i], curr)
                if next_node == -1 or dist[i] < dist[next_node]:
                    next_node = i
            res += int(dist[next_node])
            node = next_node
            edges += 1
        
        return res


    def minCostConnectPointsKruskal(self, points: list[list[int]]) -> int:
        # My solution: Kruskal's algorithm - probably O(n^2 log n)

        costs: dict[tuple[int, int], dict[tuple[int, int], int]] = {}
        edges = []

        sets = {(x, y): i for i, (x, y) in enumerate(points)}
        while points:
            xi, yi = points.pop()
            for xj, yj in points:
                costs[(xi, yi)] = {}
                costs[(xi, yi)][(xj, yj)] = abs(xi - xj) + abs(yi - yj)
                edges.append([(xi, yi), (xj, yj), costs[(xi, yi)][(xj, yj)]])

        edges.sort(key=lambda x: -x[2])
        min_cost = 0

        while edges:
            (xi, yi), (xj, yj), cost = edges.pop()
            if sets[(xi, yi)] != sets[(xj, yj)]:
                min_cost += cost
                old_set = sets[(xj, yj)]
                new_set = sets[(xi, yi)]
                for key, set in sets.items():
                    if set == old_set:
                        sets[key] = new_set
        return min_cost


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: list[list[int]], exp: int):
        res = sol.minCostConnectPoints(inp)
        print(res)
        assert res == exp

    print_and_assert([[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]], 10)
    print_and_assert([[0, 0], [1, 1], [1, 0], [-1, 1]], 4)
