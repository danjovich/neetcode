from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        max_depth = -1

        def dfs(node: Optional[TreeNode], depth=0):
            if not node:
                return

            nonlocal max_depth
            if depth > max_depth:
                max_depth = depth
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root)
        return res

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp, exp):
        res = sol.rightSideView(inp)
        print(res)
        assert res == exp

    n3 = TreeNode(3)
    n2 = TreeNode(2)
    n1 = TreeNode(1, n2, n3)
    print_and_assert(n1, [1, 3])

    n7 = TreeNode(7)
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, n6, n7)
    n2 = TreeNode(2, n4, n5)
    n1 = TreeNode(1, n2, n3)
    print_and_assert(n1, [1, 3, 7])
