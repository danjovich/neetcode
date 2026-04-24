class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1

        def dfs(root: Optional[TreeNode], known_less=0) -> int:
            nonlocal res
            if res != -1:
                return -1

            if not root:
                return known_less

            count = 1 + dfs(root.left, known_less)
            if count == k and res == -1:
                res = root.val

            if res != -1:
                return -1
            
            count += dfs(root.right, count) - count

            return count

        dfs(root)
        return res