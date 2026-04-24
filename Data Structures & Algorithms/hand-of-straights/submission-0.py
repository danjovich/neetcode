class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        n = len(hand)

        if n % groupSize != 0:
            return False
        
        hand.sort()

        m = n // groupSize
        groups = [(0, 0) for _ in range(m)]

        for card in hand:
            added = False
            for i, (val, length) in enumerate(groups):
                if length == 0 or (length < groupSize and val + 1 == card) :
                    groups[i] = (card, length + 1)
                    added = True
                    break
            if not added:
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(hand, groupSize, exp):
        res = sol.isNStraightHand(hand, groupSize)
        print(res)
        assert res == exp

    print_and_assert([1, 2, 4, 2, 3, 5, 3, 4], 4, True)
    print_and_assert([1, 2, 3, 3, 4, 5, 6, 7], 4, False)
