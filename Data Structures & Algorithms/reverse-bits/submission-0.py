class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 31

        while n:
            res += (n % 2) << i
            n >>= 1
            i -= 1

        return res


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.reverseBits(inp)
        print(bin(res))
        assert res == exp

    print_and_assert(21, 2818572288)
    print_and_assert(0b1110111, 0b11101110000000000000000000000000)
