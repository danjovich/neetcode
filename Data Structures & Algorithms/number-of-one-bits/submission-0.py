class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += n % 2
            n //= 2
        return count

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.hammingWeight(inp)
        print(res)
        assert res == exp

    print_and_assert(23, 4)
    print_and_assert(0b01111111111111111111111111111101, 30)
