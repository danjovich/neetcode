from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # node = head

        # while node is not None:
        #     curr, prev = head, None
        #     while curr is not None:
        #         prev = curr
        #         curr = curr.next

        #     temp = node.next
        #     node.next = prev
        #     node = prev
        #     if node is not None:
        #         node.next = temp

        # def recurse(h: ListNode) -> Optional[ListNode]:
        #     if h.next is None:
        #         return h

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
