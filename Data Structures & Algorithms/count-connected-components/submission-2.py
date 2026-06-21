from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        res = 0
        q = deque()
        i = 0
        while len(visited) < n:
            res += 1

            while i in visited:
                i += 1
            q.append(i)
            visited.add(i)
            
            while q:
                node = q.popleft()

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        
        return res
