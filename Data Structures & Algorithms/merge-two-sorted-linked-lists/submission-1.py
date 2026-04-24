# Definition for singly-linked list.
from typing import Optional


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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        n1, n2 = list1, list2
        ordered = None

        if not n1:
            head = n2
        elif not n2:
            head = n1
        elif n1.val <= n2.val:
            head = n1
        else:
            head = n2

        while n1 != None and n2 != None:
            if n1.val <= n2.val:
                if ordered:
                    ordered.next = n1
                ordered = n1
                n1 = n1.next
            else:
                if ordered:
                    ordered.next = n2
                ordered = n2
                n2 = n2.next

        if ordered:
            ordered.next = n1 or n2

        return head


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp1: ListNode, inp2: ListNode, exp: ListNode):
        res = sol.mergeTwoLists(inp1, inp2)
        print(res)
        assert res == exp

    n3 = ListNode(4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    m3 = ListNode(5)
    m2 = ListNode(3, m3)
    m1 = ListNode(1, m2)
    print_and_assert(n1, m1, n1)
