class Solution:
    def getLetters(self, digit: str) -> list[str]:
        d = int(digit)

        match d:
            case 2 | 3 | 4 | 5 | 6:
                to_add = (d - 2) * 3
                return [chr(ord("a") + to_add + i) for i in range(3)]
            case 7:
                return [chr(ord("p") + i) for i in range(4)]
            case 8:
                return [chr(ord("t") + i) for i in range(3)]
            case 9:
                return [chr(ord("w") + i) for i in range(4)]

        return []

    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        def dfs(digits: str, curr: str):
            if len(digits) == 0:
                if curr:
                    res.append(curr)
                return
            
            for c in self.getLetters(digits[0]):
                dfs(digits[1:], curr + c)
            
        dfs(digits, "")
        return res

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.letterCombinations(inp)
        print(res)
        assert res == exp

    print_and_assert("34", ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"])
    print_and_assert("", [])
