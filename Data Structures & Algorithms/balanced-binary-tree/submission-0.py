from typing import Optional, Tuple


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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> Tuple[int, bool]:
            if root is None:
                return (0, True)

            l_d, l_b = dfs(root.left)
            if not l_b:
                return (0, False)
            r_d, r_b = dfs(root.right)
            if not r_b:
                return (0, False)

            return (max(l_d + 1, r_d + 1), abs(l_d - r_d) <= 1)

        return dfs(root)[1]

if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp: TreeNode, exp: bool):
        res = sol.isBalanced(inp)
        print(res)
        assert res == exp

    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n6, n7)
    n2 = TreeNode(2, n4, n5)
    n1 = TreeNode(1, n2, n3)
    print_and_assert(n1, True)

    m5 = TreeNode(5)
    m4 = TreeNode(4)
    m3 = TreeNode(3, m5)
    m2 = TreeNode(2, m3, m4)
    m1 = TreeNode(1, None, m2)
    print_and_assert(m1, False)
