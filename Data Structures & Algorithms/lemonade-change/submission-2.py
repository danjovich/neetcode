class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            change[bill] += 1
            if bill != 5:
                if not change[5]:
                    return False
                change[5] -= 1

                if bill == 20:
                    if not change[10]:
                        if change[5] < 2:
                            return False
                        change[5] -= 2
                    else:
                        change[10] -= 1

        return True
