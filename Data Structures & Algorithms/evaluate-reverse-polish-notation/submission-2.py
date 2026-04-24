from typing import Callable


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        token = tokens.pop()
        op: Callable[[int, int], int]
        match token:
            case "+":
                op = lambda a, b: a + b
            case "-":
                op = lambda a, b: a - b
            case "*":
                op = lambda a, b: a * b
            case "/":
                op = lambda a, b: int(a / b)
            case _:
                return int(token)
        arg2 = self.evalRPN(tokens)
        arg1 = self.evalRPN(tokens)
        return op(arg1, arg2)

    def turnIntoInfixNotation(self, tokens: list[str]) -> str:
        token = tokens.pop()
        match token:
            case "+" | "-" | "*" | "/":
                arg2 = self.turnIntoInfixNotation(tokens)
                arg1 = self.turnIntoInfixNotation(tokens)
                return f"({arg1} {token} {arg2})"
            case _:
                return token


if __name__ == "__main__":
    sol = Solution()

    tokens = ["1", "2", "+", "3", "*", "4", "-"]
    print(sol.turnIntoInfixNotation(tokens.copy()))
    ans = sol.evalRPN(tokens)
    print(ans)
    assert ans == 5

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(sol.turnIntoInfixNotation(tokens.copy()))
    ans = sol.evalRPN(tokens)
    print(ans)
    assert ans == 22
