class Solution:
    def reverse(self, x: int) -> int:
        LIMIT = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        DIGITS_LIMIT = 10

        negative = x < 0
        if negative:
            x = -x
        res = 0
        greater_than_limit = False
        smaller_than_limit = False
        for i in range(DIGITS_LIMIT - 1):
            curr = x % 10
            if not smaller_than_limit and curr > LIMIT[i]:
                greater_than_limit = True
            elif not greater_than_limit and curr < LIMIT[i]:
                smaller_than_limit = True
            res *= 10
            res += curr
            x //= 10
            if x == 0:
                return res * (-1 if negative else 1)

        if smaller_than_limit or (
            not greater_than_limit and (x % 10 < LIMIT[9] or (not negative and x % 10 == LIMIT[9]))
        ):
            return (res * 10 + x % 10) * (-1 if negative else 1)

        return 0
