from typing import Tuple


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # using stack
        stack: list[Tuple[int, int]] = [] # stack of indexes and values
        res: list[int] = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                j, _ = stack.pop()
                res[j] = i - j

            stack.append((i, temperatures[i]))

        return res

        # # elegant, but O(n^2)

        # result: list[int] = [0] * len(temperatures)

        # for i in range(len(temperatures) - 1, -1, -1):
        #     j = i - 1
        #     while j >= 0 and temperatures[j] < temperatures[i]:
        #         result[j] = i - j
        #         j -= 1

        # return result


if __name__ == "__main__":
    sol = Solution()

    temperatures = [30, 38, 30, 36, 35, 40, 28]
    res = sol.dailyTemperatures(temperatures)
    print(res)
    assert res == [1, 4, 1, 2, 1, 0, 0]

    temperatures = [22, 21, 20]
    res = sol.dailyTemperatures(temperatures)
    print(res)
    assert res == [0, 0, 0]
