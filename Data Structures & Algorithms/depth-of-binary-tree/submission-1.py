from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: " Optional[TreeNode]" = None,
        right: " Optional[TreeNode]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        s = str(self.val)
        return f"[{s + self.str_left_and_right()}]"

    def str_left_and_right(self) -> str:
        s = ""
        if self.left:
            s += f", {self.left.val}"
        if self.right:
            s += f", {self.right.val}"
        if self.left:
            s += self.left.str_left_and_right()
        if self.right:
            s += self.right.str_left_and_right()
        return s


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        d_l = self.maxDepth(root.left) + 1
        d_r = self.maxDepth(root.right) + 1

        return max(d_l, d_r)


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: TreeNode, exp: int):
        res = sol.maxDepth(inp)
        print(res)
        assert res == exp

    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n6, n7)
    n2 = TreeNode(2, n4, n5)
    n1 = TreeNode(1, n2, n3)

    print_and_assert(n1, 3)
