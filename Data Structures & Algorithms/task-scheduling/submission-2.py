from collections import defaultdict
from heapq import heapify, heappop


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        tasks_dict: dict[str, int] = defaultdict(int)

        for task in tasks:
            tasks_dict[task] += 1

        heap = [(-count, task) for (task, count) in tasks_dict.items()]

        heapify(heap)

        exceeding = 0
        prev = None
        reallocable = 0
        while heap:
            c, _ = heappop(heap)
            c = -c
            idle = (c - 1) * n

            if prev is None or not exceeding:
                exceeding += idle - reallocable if idle >= reallocable else 0
            elif exceeding:
                exceeding -= c - 1 if c > 1 else 1
                reallocable += c - 1 if c > 1 else 1

            prev = c

        return len(tasks) + exceeding


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(tasks, n, exp):
        res = sol.leastInterval(tasks, n)
        print(res)
        assert res == exp

    print_and_assert(["X", "X", "Y", "Y"], 2, 5)
    print_and_assert(["A", "A", "A", "B", "C"], 3, 9)
    print_and_assert(
        ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2, 12
    )
