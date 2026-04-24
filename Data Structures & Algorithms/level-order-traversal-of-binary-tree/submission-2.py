class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        return self.recursiveLevelOrder(root, 0, [])

    def recursiveLevelOrder(
        self, node: TreeNode | None, level, lst: list[list[int]]
    ) -> list[list[int]]:
        if node is not None:
            if len(lst) <= level:
                lst.append([])

            lst[level].append(node.val)
            self.recursiveLevelOrder(node.left, level + 1, lst)
            self.recursiveLevelOrder(node.right, level + 1, lst)

        return lst


if __name__ == "__main__":
    sol = Solution()

    def print_and_assert(root: TreeNode, exp: list[list[int]]):
        res = sol.levelOrder(root)
        print(res)
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

    print_and_assert(n5, [[5], [3, 8], [1, 4, 7, 9], [2]])
