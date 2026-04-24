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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        s_p, s_q = [p], [q]

        while s_p and s_q:
            n_p, n_q = s_p.pop(), s_q.pop()

            if n_p.val != n_q.val:
                return False

            l_p, l_q = n_p.left, n_q.left
            if l_p and l_q:
                s_p.append(l_p)
                s_q.append(l_q)
            elif l_p != l_q:
                return False

            r_p, r_q = n_p.right, n_q.right
            if r_p and r_q:
                s_p.append(r_p)
                s_q.append(r_q)
            elif r_p != r_q:
                return False

        return s_p == s_q

if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(inp1: TreeNode, inp2: TreeNode, exp: bool):
        res = sol.isSameTree(inp1, inp2)
        print(res)
        assert res == exp

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
    m3 = TreeNode(3, m6, m7)
    m2 = TreeNode(2, m4, m5)
    m1 = TreeNode(1, m2, m3)
    print_and_assert(n1, m1, True)

    o5 = TreeNode(5)
    o4 = TreeNode(4)
    o3 = TreeNode(3, o5)
    o2 = TreeNode(2, o3, o4)
    o1 = TreeNode(1, None, o2)
    print_and_assert(m1, o1, False)
