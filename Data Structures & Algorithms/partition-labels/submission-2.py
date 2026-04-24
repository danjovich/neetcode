class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        f_and_l: dict[str, tuple[int, int]] = {}
        for i, c in enumerate(s):
            if f_and_l.get(c) is None:
                f_and_l[c] = (i, i)
            else:
                f_and_l[c] = (f_and_l[c][0], i)

        curr_last = -1
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            first, last = f_and_l[c]
            if first < curr_last and last > curr_last:
                res[-1] += last - curr_last
                curr_last = last
            elif last <= curr_last:
                pass
            elif first == last:
                res.append(1)
            else:
                res.append(last - first + 1)
                curr_last = last
            i += 1

        return res