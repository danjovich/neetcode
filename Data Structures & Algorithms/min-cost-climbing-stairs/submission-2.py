class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        min_per_len: list[int | None] = [None] * (len(cost) + 1)

        def backtrack(cost: list[int]) -> int:
            nonlocal min_per_len
            if (res := min_per_len[len(cost)]) is not None:
                return res
            if len(cost) <= 1:
                return 0
            if len(cost) == 2:
                res = min(cost)
                min_per_len[len(cost)] = res
                return res
            if len(cost) == 3:
                res = min(cost[1], cost[0] + cost[2])
                min_per_len[len(cost)] = res
                return res

            cost1 = cost[0] + cost[1] + backtrack(cost[2:])
            cost2 = cost[0] + cost[2] + backtrack(cost[3:])
            cost3 = cost[1] + cost[2] + backtrack(cost[3:])
            cost4 = cost[1] + cost[3] + backtrack(cost[4:])

            res = min(cost1, cost2, cost3, cost4)
            min_per_len[len(cost)] = res
            return res

        return backtrack(cost)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.minCostClimbingStairs(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 3], 2)
    print_and_assert([1, 2, 1, 2, 1, 1, 1], 4)
    print_and_assert([0, 1, 0, 1], 0)
