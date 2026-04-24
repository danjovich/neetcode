class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pos_spd = [(pos, spd) for pos, spd in zip(position, speed)]

        pos_spd.sort(key=lambda ps: -ps[0])
        fleets: list[float] = []

        for pos, spd in pos_spd:
            time = (target - pos) / spd

            if not fleets or fleets[-1] < time:
                fleets.append(time)

        return len(fleets)

        # O(n^2)
        # times_t: list[Tuple[int, float]] = []
        # times: list[float] = []

        # for i, (pos, spd) in enumerate(zip(position, speed)):
        #     time = (target - pos) / spd
        #     times_t.append((i, time))
        #     times.append(time)

        # times_t.sort(key=lambda tup: tup[1])

        # for i, (index1, time1) in enumerate(times_t):
        #     for index2, _ in times_t[:i]:
        #         if position[index2] < position[index1]:
        #             times[index2] = time1

        # return len({time for time in times})


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
