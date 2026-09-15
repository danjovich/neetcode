from collections import defaultdict, deque


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, i))
            graph[b].append((a, i))

        res = -1
        visited_nodes, visited_edges = set(), set()

        def dfs(node: int) -> bool:
            nonlocal res
            visited_nodes.add(node)

            found_loop = False
            for neighbor, i in graph[node]:
                if i in visited_edges:
                    continue

                visited_edges.add(i)
                if neighbor in visited_nodes or dfs(neighbor):
                    res = max(i, res)
                    found_loop = True

            return found_loop

        dfs(edges[0][0])
        return edges[res]
