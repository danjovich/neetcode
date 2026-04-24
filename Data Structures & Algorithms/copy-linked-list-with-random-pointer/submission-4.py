from typing import Optional, cast
import uuid


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        node = head
        while node:
            node.hash = str(uuid.uuid4())  # pyright: ignore[reportAttributeAccessIssue]
            node.__hash__ = lambda: hash(
                cast(Node, node).hash  # pyright: ignore[reportAttributeAccessIssue]
            )
            node = node.next

        node = head
        new_head = Node(node.val)
        new_node = new_head
        orig_to_new = {node: new_node}

        if node.random and (existing := orig_to_new.get(node.random)):
                new_node.random = existing
        elif node.random:
            new_node.random = Node(node.random.val)
            orig_to_new[node.random] = new_node.random

        node = node.next
        while node:
            if existing := orig_to_new.get(node):
                new_node.next = existing
            else:
                new_node.next = Node(node.val)
                orig_to_new[node] = new_node.next

            if node.random and (existing := orig_to_new.get(node.random)):
                new_node.next.random = existing
            elif node.random:
                new_node.next.random = Node(node.random.val)
                orig_to_new[node.random] = new_node.next.random

            node = node.next
            new_node = new_node.next

        return new_head


if __name__ == "__main__":
    sol = Solution()

    def generate_linked_list(source: list[list[Optional[int]]]) -> Optional[Node]:
        if not source:
            return None

        head = Node(cast(int, source[0][0]))
        node = head
        nodes = [node]

        for i in range(1, len(source)):
            node.next = Node(cast(int, source[i][0]))
            node = node.next
            nodes.append(node)

        for i, (_, random) in enumerate(source):
            if random is not None:
                nodes[i].random = nodes[random]

        return head

    def print_and_assert(inp):
        inp = generate_linked_list(inp)
        res = sol.copyRandomList(inp)

        while inp and res:
            random = inp.random.val if inp.random else "None"
            print(
                f"Expected: val = {inp.val}, random = {random};",
                end=" ",
            )

            random = res.random.val if res.random else "None"
            print(f"Actual: val = {res.val}, random = {random}")

            assert res.val == inp.val
            assert hash(res) != hash(inp)
            assert (inp.random.val if inp.random else None) == (
                res.random.val if res.random else None
            )

            res = res.next
            inp = inp.next
        print()

    print_and_assert([[3, None], [7, 3], [4, 0], [5, 1]])
    print_and_assert([[1, None], [2, 2], [3, 2]])
    print_and_assert([[-1, 0]])
