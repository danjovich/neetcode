# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#              5
#          4        8
#        11      13   4
#      7   2       1

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def recurse(root: Optional[TreeNode]) -> int:
            nonlocal res
            left, right = None, None
            local_res = root.val

            if root.left:
                left = recurse(root.left)
                local_res = max(local_res, root.val + left)

            if root.right:
                right = recurse(root.right)
                local_res = max(local_res, root.val + right)

            res = max(res, local_res)
            if left and right:
                    res = max(res, root.val + right + left)
            return local_res
        recurse(root)
        return res
