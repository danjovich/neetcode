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


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseListConfusingSolution(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if head is None:
            return None

        node = head
        next_node = node.next
        node.next = None
        while next_node:
            temp = next_node.next
            next_node.next = node
            if not temp:
                node = next_node
                break
            node = temp
            temp = next_node
            next_node = node.next
            node.next = temp
        return node


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: ListNode, exp: ListNode):
        res = sol.reverseList(inp)
        print(res)
        assert res == exp

    n4 = ListNode(3)
    n3 = ListNode(2, n4)
    n2 = ListNode(1, n3)
    n1 = ListNode(0, n2)
    print_and_assert(n1, n4)

    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print_and_assert(n1, n5)
