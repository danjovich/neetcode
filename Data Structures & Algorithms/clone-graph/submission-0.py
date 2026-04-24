from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited: dict[int, Node] = {}

        def dfs(node: Optional["Node"]) -> Optional["Node"]:
            if node is None:
                return None
            if visited.get(node.val):
                return visited[node.val]

            node_clone = Node(node.val)
            visited[node.val] = node_clone

            for neighbor in node.neighbors:
                node_clone.neighbors.append(dfs(neighbor))

            return node_clone

        return dfs(node)

if __name__ == "__main__":
    sol = Solution()
    def print_and_assert(inp: Node):
        res = sol.cloneGraph(inp)
        print(res)
        if not res:
            assert inp is None
            return
        visited = set()
        def dfs(res: Node, exp: Node):
            assert res != exp, "The Nodes can't be the same reference"
            assert res.val == exp.val, f"res: {res.val} != exp: {exp.val}"
            if res.val in visited:
                return
            visited.add(res.val)
            for n_res, n_exp in zip(res.neighbors, exp.neighbors):
                dfs(n_res, n_exp)
        dfs(res, inp)

    n3 = Node(3)
    n2 = Node(2, [n3])
    n1 = Node(1, [n2])
    print_and_assert(n1)
