class Solution:
    def isValid(self, s: str) -> bool:
        brackets: list[str] = list()

        l_brackets = {")": "(", "}": "{", "]": "["}

        for c in s:
            match c:
                case "(" | "{" | "[":
                    brackets.append(c)
                case ")" | "}" | "]":
                    if len(brackets) == 0:
                        return False
                    l_bracket = brackets.pop()
                    if l_brackets[c] != l_bracket:
                        return False
                case _:
                    pass

        return len(brackets) == 0


if __name__ == "__main__":
    sol = Solution()

    s = "[]"
    assert sol.isValid(s)

    s = "([{}])"
    assert sol.isValid(s)

    s = "[(])"
    assert not sol.isValid(s)
