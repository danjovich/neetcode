class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            s = s.replace("#", "\\#/")
            res += s + f"#{len(s)}#"

        return res

    def decode(self, s: str) -> list[str]:
        if len(s) == 0:
            return []

        res = []
        curr = ""
        curr_len = ""
        found_pattern = False
        for i in range(len(s)):
            c = s[i]
            if found_pattern:
                if c == "#":
                    res.append(curr.replace("\\#/", "#"))
                    curr = ""
                    found_pattern = False
                else:
                    try:
                        int(c)
                        curr_len += c
                    except ValueError:
                        found_pattern = False
                        curr += f"#{curr_len}{c}"
            else:
                if (
                    c == "#"
                    and (i == 0 or i != len(s) - 1)
                    and not (s[i - 1] == "\\" and s[i + 1] == "/")
                ):
                    found_pattern = True
                else:
                    curr += c

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.decode(sol.encode(["neet", "code", "love", "you"])))
    # print(sol.encode(["neet", "code", "love", "you"]))

    print(sol.decode(sol.encode(["we", "say", ":", "yes"])))
    # print(sol.encode(["we", "say", ":", "yes"]))

    print(sol.decode(sol.encode(["we\\", "say", ":", "yes"])))
    # print(sol.encode(["we\\", "say", ":", "yes"]))

    print(sol.decode(sol.encode(['we", ', "say", ":", "yes"])))
    # print(sol.encode(['we", ', "say", ":", "yes"]))

    print(sol.decode(sol.encode(['\\#/1#/", ', "say", ":", "yes"])))

    print(sol.decode(sol.encode(["we", "say", ":", "yes", "!@#$%^&*()"])))
