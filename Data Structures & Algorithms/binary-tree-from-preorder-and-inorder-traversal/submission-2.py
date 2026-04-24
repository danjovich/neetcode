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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        #     1
        #  2     3
        # 4 5   6 7
        #    8
        # preorder = [1, 2, 4, 5, 8, 3, 6, 7]
        # inorder = [4, 2, 5, 8, 1, 6, 3, 7]

        inorder_is = {v: i for i, v in enumerate(inorder)}

        p = 0
        def dfs(l: int, r: int) -> TreeNode:
            nonlocal p
            if r < l:
                return None

            root_val = preorder[p]
            root_i = inorder_is[root_val]
            p += 1

            root = TreeNode(root_val)
            root.left = dfs(l, root_i - 1)
            root.right = dfs(root_i + 1, r)

            return root

        return dfs(0, len(preorder) - 1)