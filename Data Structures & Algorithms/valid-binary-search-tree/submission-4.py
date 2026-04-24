import math
from typing import Optional


# Definition for a binary tree node.
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], min_value: int | float, max_value: int | float) -> bool:
            if not root:
                return True

            if root.left and (root.left.val >= root.val or root.left.val <= min_value):
                return False

            if root.right and (
                root.right.val <= root.val or root.right.val >= max_value
            ):
                return False

            return dfs(root.left, min_value, root.val) and dfs(
                root.right, root.val, max_value
            )

        return dfs(root, -math.inf, math.inf)


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
        res = sol.isValidBST(root)
        print(res)
        assert res == exp

    print_and_assert([2, 1, 3], True)
    print_and_assert([1, 2, 3], False)
    print_and_assert([5, 4, 6, None, None, 3, 7], False)
    print_and_assert([3, 1, 5, 0, 2, 4, 6], True)
    print_and_assert([3, 1, 5, 0, 2, 4, 6, None, None, None, 3], False)
