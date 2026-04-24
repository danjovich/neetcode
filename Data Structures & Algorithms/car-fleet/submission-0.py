from typing import Tuple


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        times_t: list[Tuple[int, float]] = []
        times: list[float] = []

        for i, (pos, spd) in enumerate(zip(position, speed)):
            time = (target - pos) / spd
            times_t.append((i, time))
            times.append(time)

        times_t.sort(key=lambda tup: tup[1])

        for i, (index1, time1) in enumerate(times_t):
            for index2, _ in times_t[:i]:
                if position[index2] < position[index1]:
                    times[index2] = time1

        return len({time for time in times})

        # i = len(times) - 1
        # while i >= 0:
        #     j = i - 1
        #     while j > 0:
        #         i_i, time_i = times[i]
        #         i_j, time_j = times[j]

        #         if time_i > time_j and position[i_i] > position[i_j]:
        #             times[j] = (j, time_i)
        #         j -= 1
        #     i -= 1

        # fleets: set[int] = set()
        # for _, time in times:
        #     fleets.add(time)

        # return len(fleets)


if __name__ == "__main__":
    sol = Solution()

    target = 10
    position = [1, 4]
    speed = [3, 2]
    out = sol.carFleet(target, position, speed)
    print(out)
    assert out == 1

    target = 10
    position = [4, 1, 0, 7]
    speed = [2, 2, 1, 1]
    out = sol.carFleet(target, position, speed)
    print(out)
    assert out == 3
