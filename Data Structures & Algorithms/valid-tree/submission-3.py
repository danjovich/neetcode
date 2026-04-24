from collections import defaultdict, deque


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        graph = defaultdict(list)

        for n1, n2 in edges:
            if n2 not in graph:
                graph[n1].append(n2)
            elif n1 not in graph:
                graph[n2].append(n1)
            else:
                return False
        
        if not graph:
            return n <= 1
        
        q = deque()
        q.append(list(graph.keys())[0])
        visited = set()
        while q:
            node = q.popleft()

            if node in visited:
                return False
            visited.add(node)

            for neighbor in graph[node]:
                q.append(neighbor)


        return len(visited) == n