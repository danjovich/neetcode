class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        a, b, c = target
        found_a, found_b, found_c = False, False, False

        i = 0
        while i < len(triplets) and not (found_a and found_b and found_c):
            a_i, b_i, c_i = triplets[i]

            found_a = found_a or (a_i == a and b_i <= b and c_i <= c)
            found_b = found_b or (a_i <= a and b_i == b and c_i <= c)
            found_c = found_c or (a_i <= a and b_i <= b and c_i == c)

            i += 1

        return found_a and found_b and found_c


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(triplets, target, exp):
        res = sol.mergeTriplets(triplets, target)
        print(res)
        assert res == exp

    print_and_assert([[1, 2, 3], [7, 1, 1]], [7, 2, 3], True)
    print_and_assert([[2,5,6],[1,4,4],[5,7,5]], [5,4,6], False)
