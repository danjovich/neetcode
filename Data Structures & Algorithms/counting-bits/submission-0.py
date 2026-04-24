class Solution:
    def countBits(self, n: int) -> list[int]:
        output = []
        for i in range(n + 1):
            output.append(bin(i).count('1'))
        return output


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: int, exp: list[int]):
        res = sol.countBits(inp)
        print(res)
        assert res == exp

    print_and_assert(4, [0, 1, 1, 2, 1])
