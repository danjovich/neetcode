from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        s = str(self.val)
        next = self.next
        while next is not None:
            s += f" -> {str(next.val)}"
            next = next.next
        return s

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()

        while head:
            temp = head.next
            if temp == dummy:
                return True
            head.next = dummy
            head = temp

        return False

if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: ListNode, exp: bool):
        res = sol.hasCycle(inp)
        print(res)
        assert res == exp

    n4 = ListNode(4)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    n4.next = n1
    print_and_assert(n1, True)

    n2 = ListNode(2)
    n1 = ListNode(1, n2)
    print_and_assert(n1, False)
