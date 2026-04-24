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
        if len(preorder) == 0 or len(inorder) == 0:
            return None

        root_i = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1 : root_i + 1], inorder[:root_i])
        root.right = self.buildTree(preorder[root_i + 1 :], inorder[root_i + 1 :])

        return root