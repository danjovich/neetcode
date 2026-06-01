from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        
        q = deque([root])
        s = {root} if root is not None else {}
        none_count = 0
        while s:
            node = q.popleft()
            if node:
                if none_count > 0:
                    res += f"N{none_count}#"
                    none_count = 0
                s.remove(node)
                res += f"{node.val}#"
            else:
                none_count += 1
                continue

            q.append(node.left)
            if node.left:
                s.add(node.left)

            q.append(node.right)
            if node.right:
                s.add(node.right)

        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        vals = data.split("#")
        root = parent = TreeNode(int(vals[0]))
        q = deque()
        is_left = True
        for val in vals[1:-1]:
            if val[0] != "N":
                node = TreeNode(int(val))
                q.append(node)
                if is_left:
                    parent.left = node
                else:
                    parent.right = node
                is_left = not is_left
                if is_left:
                    parent = q.popleft()
            else:
                nones = int(val[1:])
                for _ in range(nones):
                    is_left = not is_left
                    if is_left:
                        parent = q.popleft()

        return root
