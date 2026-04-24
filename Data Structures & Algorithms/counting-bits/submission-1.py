class Solution:
    def countBits(self, n: int) -> list[int]:
        # non-recursive dynamic programming solution,
        # based on the recursive one below
        # time: O(n), space: O(1)

        output = [0] * (n + 1)
        for i in range(1, n + 1):
            output[i] = output[i >> 1] + i % 2
        return output

    def countBitsRecursive(self, n: int) -> int:
        if n <= 1:
            return n

        # the number of 1 bits of n is the same as the number
        # of 1 bits of n >> 1 plus the 1 in the least significant
        # bit, if there is such bit
        return self.countBitsRecursive(n >> 1) + n % 2

    def countBitsUsingRecursive(self, n: int) -> list[int]:
        output = []
        for i in range(n + 1):
            output.append(self.countBitsRecursive(i))
        return output

    def countBitsUsingBuiltin(self, n: int) -> list[int]:
        output = []
        for i in range(n + 1):
            output.append(bin(i).count("1"))
        return output


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: int, exp: list[int]):
        res = sol.countBits(inp)
        print(res)
        assert res == exp

    print_and_assert(4, [0, 1, 1, 2, 1])
