class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # solution by backtracking
        stack: list[str] = []
        res: list[str] = []

        def backtrack(open: int, closed: int):
            if n == open == closed:
                res.append("".join(stack))

            if open < n:
                stack.append("(")
                backtrack(open + 1, closed)
                # remove the added "(" as the recursive call
                # will already add the resulting string to
                # the res array
                stack.pop()

            if closed < open:
                stack.append(")")
                backtrack(open, closed + 1)
                # same here
                stack.pop()

        backtrack(0, 0)
        return res


if __name__ == "__main__":

    def print_and_assert(actual: list[str], expected: list[str]):
        print(actual)
        assert len(actual) == len(expected)
        expected_set = set(expected)
        assert len(set(actual)) == len(expected_set)
        for s in actual:
            assert s in expected_set

    sol = Solution()

    inp = 1
    res = sol.generateParenthesis(inp)
    print_and_assert(res, ["()"])

    inp = 3
    res = sol.generateParenthesis(inp)
    print_and_assert(res, ["((()))", "(()())", "(())()", "()(())", "()()()"])
