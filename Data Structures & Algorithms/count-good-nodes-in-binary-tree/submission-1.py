# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, curr_max: Optional[int] = None) -> int:
            count = 0
            if curr_max is None or node.val >= curr_max:
                curr_max = node.val
                count += 1

            count += dfs(node.left, curr_max) if node.left else 0
            count += dfs(node.right, curr_max) if node.right else 0

            return count

        return dfs(root)


if __name__ == "__main__":
    sol = Solution()

    def generate_tree(values: list[Optional[int]]) -> TreeNode:
        assert values, "The tree must not be empty"
        assert values[0] is not None, "The tree root must not be empty"

        root = TreeNode(values[0])

        def dfs(root: TreeNode, i: int):
            left_i = i * 2 + 1
            left = (
                TreeNode(val)
                if left_i < len(values) and (val := values[left_i]) is not None
                else None
            )
            if left:
                root.left = left
                dfs(left, left_i)

            right_i = left_i + 1
            right = (
                TreeNode(val)
                if right_i < len(values) and (val := values[right_i]) is not None
                else None
            )
            if right:
                root.right = right
                dfs(right, right_i)

        dfs(root, 0)

        return root

    def print_and_assert(inp, exp):
        root = generate_tree(inp)
        res = sol.goodNodes(root)
        print(res)
        assert res == exp

    print_and_assert([3, 1, 4, 3, None, 1, 5], 4)
    print_and_assert([2, 1, 1, 3, None, 1, 5], 3)
    print_and_assert([1, 2, -1, 3, 4], 4)
