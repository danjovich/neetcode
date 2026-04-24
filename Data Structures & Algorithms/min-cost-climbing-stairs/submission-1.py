class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) <= 1:
            return 0
        if len(cost) == 2:
            return min(cost)
        if len(cost) == 3:
            return min(cost[1], cost[0] + cost[2])

        cost1 = cost[0] + cost[1] + self.minCostClimbingStairs(cost[2:])
        cost2 = cost[0] + cost[2] + self.minCostClimbingStairs(cost[3:])
        cost3 = cost[1] + cost[2] + self.minCostClimbingStairs(cost[3:])
        cost4 = cost[1] + cost[3] + self.minCostClimbingStairs(cost[4:])

        return min(cost1, cost2, cost3, cost4)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.minCostClimbingStairs(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 3], 2)
    print_and_assert([1, 2, 1, 2, 1, 1, 1], 4)
    print_and_assert([0, 1, 0, 1], 0)
