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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if (
            root.val == subRoot.val
            and self.isSameTree(root.left, subRoot.left)
            and self.isSameTree(root.right, subRoot.right)
        ):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False

        return (
            tree1.val == tree2.val
            and self.isSameTree(tree1.left, tree2.left)
            and self.isSameTree(tree1.right, tree2.right)
        )


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp1: TreeNode, inp2: TreeNode, exp: bool):
        res = sol.isSubtree(inp1, inp2)
        print(res)
        assert res == exp

    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n4, n5)
    n1 = TreeNode(1, n2, n3)

    m5 = TreeNode(5)
    m4 = TreeNode(4)
    m2 = TreeNode(2, m4, m5)
    print_and_assert(n1, m2, True)

    n6 = TreeNode(6)
    n4.left = n6
    print_and_assert(n1, m2, False)

    n5 = TreeNode(2)
    n4 = TreeNode(1)
    n3 = TreeNode(5, n5)
    n2 = TreeNode(4, n4)
    n1 = TreeNode(3, n2, n3)

    m5 = TreeNode(2)
    m4 = TreeNode(1)
    m2 = TreeNode(3, m4, m5)
    print_and_assert(n1, m2, False)
