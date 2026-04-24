from math import ceil
from typing import Optional, cast


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        n = 0
        node = head
        while node is not None:
            node = node.next
            n += 1

        rvd: ListNode = head  # pyright: ignore[reportRedeclaration]
        prev = None
        for i in range(ceil(n / 2)):
            prev = rvd
            rvd = cast(ListNode, rvd.next)
        if prev:
            prev.next = None
        # head is now the first half

        prev = None
        while rvd.next and rvd.next.next:
            next = rvd.next
            rvd.next = prev
            next_next = next.next
            next.next = rvd
            prev = next
            rvd = cast(ListNode, next_next)
        if rvd.next:
            temp = prev
            prev = rvd
            rvd = rvd.next
            rvd.next = prev
            prev.next = temp
        else:
            rvd.next = prev
        # rvd is now the second half reversed

        rvd: Optional[ListNode] = rvd
        while head and rvd:
            next_head = head.next
            next_rvd = rvd.next
            head.next = rvd
            rvd.next = next_head
            head = next_head
            rvd = next_rvd

    def reorderListFirstSolution(self, head: Optional[ListNode]) -> None:
        def last(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = head
            while head:
                if head.next is None:
                    if prev:
                        prev.next = None
                    return head
                prev = head
                head = head.next

        node = head
        while node and node.next and node.next.next:
            temp = node.next
            node.next = last(temp)
            if node.next:
                node.next.next = temp
            node = temp


if __name__ == "__main__":
    sol = Solution()

    def generate_linked_list(inp: list[int]):
        prev, node, head = None, None, None
        for v in inp:
            node = ListNode(v, None)
            if not head:
                head = node
            if prev is not None:
                prev.next = node
            prev = node
        return head

    def print_and_assert(inp, exp):
        i = generate_linked_list(inp)
        e = generate_linked_list(exp)
        sol.reorderList(i)
        while i is not None and e is not None:
            print(i.val, e.val)
            assert i.val == e.val
            i, e = i.next, e.next
        print()
        assert i == e

    print_and_assert([2, 4, 6, 8], [2, 8, 4, 6])
    print_and_assert([2, 4, 6, 8, 10], [2, 10, 4, 8, 6])
