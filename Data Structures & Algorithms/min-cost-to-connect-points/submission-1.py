class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
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
