# Definition for a binary tree node.
from typing import Optional


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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)

        return root

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp: TreeNode, exp: TreeNode):
        res = sol.invertTree(inp)
        print(res)
        assert str(res) == str(exp)

    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n6, n7)
    n2 = TreeNode(2, n4, n5)
    n1 = TreeNode(1, n2, n3)

    m7 = TreeNode(7)
    m6 = TreeNode(6)
    m5 = TreeNode(5)
    m4 = TreeNode(4)
    m3 = TreeNode(3, m7, m6)
    m2 = TreeNode(2, m5, m4)
    m1 = TreeNode(1, m3, m2)
    print_and_assert(n1, m1)
