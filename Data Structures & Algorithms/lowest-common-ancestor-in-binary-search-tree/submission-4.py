class TreeNode:
    def __init__(
        self, val=0, left: "TreeNode | None" = None, right: "TreeNode | None" = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode | None, p: TreeNode | None, q: TreeNode | None
    ) -> TreeNode | None:
        if not root or not p or not q:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(root: TreeNode, p: TreeNode, q: TreeNode, exp: TreeNode):
        res = sol.lowestCommonAncestor(root, p, q)
        print(res.val if res else res)
        assert res == exp
        assert res == exp

    n2 = TreeNode(2)
    n9 = TreeNode(9)
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n1 = TreeNode(1, None, n2)
    n8 = TreeNode(8, n7, n9)
    n3 = TreeNode(3, n1, n4)
    n5 = TreeNode(5, n3, n8)

    print_and_assert(n5, n3, n8, n5)
    print_and_assert(n5, n3, n4, n3)
