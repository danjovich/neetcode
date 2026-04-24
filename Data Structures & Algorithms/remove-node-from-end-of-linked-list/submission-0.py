from typing import Optional, cast


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        length = 0
        node = head
        while node and node.next:
            node = node.next
            length += 1
        length += 1

        if length == n:
            return head.next

        prev, node = None, head
        for _ in range(length - n):
            prev = node
            node = cast(ListNode, node.next)

        if prev:
            prev.next = node.next

        return head


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

    def print_and_assert(inp, n, exp):
        inp = generate_linked_list(inp)
        exp = generate_linked_list(exp)

        res = sol.removeNthFromEnd(inp, n)
        while res is not None and exp is not None:
            print(res.val, exp.val)
            assert res.val == exp.val
            res, exp = res.next, exp.next

        print(res, exp)
        assert res == exp
        print()

    print_and_assert([1, 2, 3, 4], 2, [1, 2, 4])
    print_and_assert([5], 1, [])
    print_and_assert([1, 2], 2, [2])
