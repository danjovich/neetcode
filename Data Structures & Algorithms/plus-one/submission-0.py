class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = True
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                carry = False
                break
        return digits if not carry else [1] + digits


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp, exp):
        res = sol.plusOne(inp)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 3, 4], [1, 2, 3, 5])
    print_and_assert([9, 9, 9], [1, 0, 0, 0])
