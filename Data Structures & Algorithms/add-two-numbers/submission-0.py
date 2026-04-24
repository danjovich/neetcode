from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        l3 = ListNode()
        curr, prev = l3, None
        carry = 0
        while l1 or l2 or carry:
            v1, v2 = l1.val if l1 else 0, l2.val if l2 else 0
            res = v1 + v2 + carry
            carry = res // 10
            res -= carry * 10
            curr.val = res
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        if prev:
            prev.next = None

        return l3
