# TODO: is there a universal solution for this problem in which
# it is impossible to trick with the scape string?
class Solution:
    def encode(self, strs: list[str]) -> str:
        # O(n * m), m = average string length

        res = ""
        for s in strs:
            res += f"{len(s)}#" + s

        return res

    def decode(self, s: str) -> list[str]:
        # O(n * m), m = average string length

        res = []
        curr = ""
        curr_len = ""
        curr_len_int = 0
        reading_len = True
        for i in range(len(s)):
            c = s[i]
            if reading_len:
                if c == "#":
                    curr_len_int = int(curr_len)
                    if curr_len_int == 0:
                        curr_len = ""
                        res.append("")
                        continue

                    reading_len = False
                    curr_len = ""
                else:
                    curr_len += c
            else:
                if curr_len_int > 0:
                    curr += c

                if curr_len_int > 1:
                    curr_len_int -= 1
                else:
                    res.append(curr)
                    reading_len = True
                    curr = ""

        if len(s) > 0 and len(res) == 0:
            res.append(curr)

        return res


if __name__ == "__main__":
    sol = Solution()
    inp = ["neet", "code", "love", "you"]
    res = sol.decode(sol.encode(inp))
    assert res == inp

    inp = ["we", "say", ":", "yes"]
    res = sol.decode(sol.encode(inp))
    assert res == inp

    inp = ["we\\", "say", ":", "yes"]
    res = sol.decode(sol.encode(inp))
    assert res == inp

    inp = ['we", ', "say", ":", "yes"]
    res = sol.decode(sol.encode(inp))
    assert res == inp

    inp = ['\\#/1#/", ', "123#say", ":", "yes"]
    res = sol.decode(sol.encode(inp))
    assert res == inp

    inp = ["we", "say", ":", "abcdefghijklm", "!@#$%^&*()"]
    res = sol.decode(sol.encode(inp))
    assert res == inp

    inp = [""]
    res = sol.decode(sol.encode(inp))
    assert res == inp

    inp = [
        "",
        "   ",
        "!@#$%^&*()_+",
        "LongStringWithNoSpaces",
        "Another, String With, Commas",
    ]
    res = sol.decode(sol.encode(inp))
    assert res == inp
