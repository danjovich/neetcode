class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        tank = 0
        start = -1
        tank_til_start = 0
        for i in range(len(gas)):
            curr = gas[i] - cost[i]
            if curr >= 0 and (start == -1 or (tank < tank_til_start and start != -1)):
                start = i
                tank_til_start = tank
            tank += curr

        return start if tank >= 0 else -1


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(gas, cost, exp):
        res = sol.canCompleteCircuit(gas, cost)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 3, 4], [2, 2, 4, 1], 3)
    print_and_assert([1, 2, 3], [2, 3, 2], -1)
    print_and_assert([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3)
    print_and_assert([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4)
    print_and_assert([2], [2], 0)
